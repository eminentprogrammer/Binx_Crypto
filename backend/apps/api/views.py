import json
import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .auth import baseURL, headers, SME_TOKEN
from django.views.decorators.csrf import csrf_exempt


def api(request):
    response_data = {
        'status'    : 'success',
        'server'    : 'Binx Crypto',
        'message'   : 'API is Live',
    }
    return JsonResponse(response_data, safe=False)


@csrf_exempt
def get_banks(request):
    url = f"{baseURL}/bank?currency=NGN&transferRecipient=false&country=Nigeria"

    try:
        res = requests.get(url, headers=headers)
        res.json()
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        response_data = {
            'status':'failure',
            'message': e
        }
        return JsonResponse(response_data, safe=False)


def make_transfer(request):
    if request.method == "POST":
        data        = json.loads(request.body)
        account     = data.get('recipient')
        bank        = data.get('bank')
        url         = f"{baseURL}/bank/resolve?account_number={account}&bank_code={bank}&currency=NGN"

        try:
            res = requests.get(url, headers=headers).json()
            return JsonResponse(res, safe=False)        
        except Exception as e:
            response_data = {
                'status':'failure',
                'message': str(e)
            }
            return JsonResponse(response_data, safe=False)
    else:
        response_data = {
            'status':'failure',
            'message': 'Invalid request'
        }
        return JsonResponse(response_data, safe=False)

    
def buy_data(request):
    if request.method == "POST":
        data            = json.load(request.body)
        phone           = data.phone
        plan            = data.plan
        network         = data.network
        TOKEN           = SME_TOKEN
        SMEURL          = "https://smedata.ng/wp-json/api/v1"
        url             = f"{SMEURL}/data?token={TOKEN}&network={network}&phone={phone}&size={plan}"
        res             = requests.get(url=url, headers=headers).json()

        response_data   = {
            "status": "successful",
            "message": res['message']
        }
        return JsonResponse(response_data, safe=False)
    else:
        response_data = {
            "status"    : "404",
            "message"   : "Invalid Request"
        }
        return JsonResponse(response_data, safe=False)
