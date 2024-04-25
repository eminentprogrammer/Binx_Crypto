import json
import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.paystack.utils import load_lib
from .auth import *

PayStackAPI = load_lib()
paystack_instance = PayStackAPI()


def api(request):
    response_data = {
        'status'    : 'success',
        'server'    : 'Binx Crypto',
        'message'   : 'API is Live',
    }
    return JsonResponse(response_data, safe=False)


# @csrf_exempt
def listBanks(request):
    banks = paystack_instance.list_banks()
    return JsonResponse(banks, safe=False)


def make_transfer(request):
    payload = {}
    if request.method == "POST":
        data        = json.loads(request.body)
        
        payload['bank_code'] = data.get('bank')
        payload['account_number'] = data.get('recipient')
            
        account_info = paystack_instance.resolve_account(payload)
        return JsonResponse(account_info, safe=True)

    
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