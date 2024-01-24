import os
import json
import environ
import requests
from pathlib import Path
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


env = environ.Env(DEBUG=(bool, False))
BASE_DIR = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

PAYSTACK_URL        = env("PAYSTACK_URL")
PAYSTACK_PUBLIC_KEY = env("PAYSTACK_TEST_KEY")
KUDA_LIVE_URL       = env("KUDA_LIVE_URL")
KUDA_TEST_URL       = env("KUDA_TEST_URL")
KUDA_API_KEY        = env("KUDA_API_KEY")
SME_TOKEN           = env("SME_TOKEN")
PAYSTACK_HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Authorization": f"Bearer {PAYSTACK_PUBLIC_KEY}",
}
SME_HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
}

def api(request):
    response_data = {
        'status'    : 'success',
        'server'    : 'Binx Crypto',
        'message'   : 'API is Live',
    }
    return JsonResponse(response_data, safe=False)


# @csrf_exempt
def get_banks(request):
    url = f"{PAYSTACK_URL}/bank?currency=NGN&transferRecipient=false&country=Nigeria"
    try:
        res = requests.get(url, headers=PAYSTACK_HEADERS)
        res.json()
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        response_data = {
            'status':'failure',
            'message': e
        }
        return JsonResponse(response_data, safe=True)


def make_transfer(request):
    if request.method == "POST":
        data        = json.loads(request.body)
        account     = data.get('recipient')
        bank        = data.get('bank')
        url         = f"{PAYSTACK_URL}/bank/resolve?account_number={account}&bank_code={bank}&currency=NGN"
        try:
            res = requests.get(url, headers=PAYSTACK_HEADERS).json()
            return JsonResponse(res, safe=True)        
        except Exception as e:
            response_data = {
                'status':'failure',
                'message': str(e)
            }
            return JsonResponse(response_data, safe=True)
    else:
        response_data = {
            'status':'failure',
            'message': 'Invalid request'
        }
        return JsonResponse(response_data, safe=True)

    
def buy_data(request):
    if request.method == "POST":
        data            = json.load(request.body)
        phone           = data.recipient
        plan            = data.plan
        network         = data.network
        TOKEN           = SME_TOKEN
        SMEURL          = "https://smedata.ng/wp-json/api/v1"
        url             = f"{SMEURL}/data?token={TOKEN}&network={network}&phone={phone}&size={plan}"
        res             = requests.get(url=url, headers=SME_HEADERS).json()
        response_data   = {
            "status": "successful",
            "message": res['message']
        }
        return JsonResponse(response_data, safe=True)
    else:
        response_data = {
            "status"    : "404",
            "message"   : "Invalid Request"
        }
        return JsonResponse(response_data, safe=True)