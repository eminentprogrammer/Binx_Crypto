import json
import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.paystack.utils import load_lib
from .auth import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, permissions, status

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
class listBanks(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, format=None):
        banks = paystack_instance.list_banks()
        return JsonResponse(banks, safe=False)

class make_transfer(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, format=None):
        data = request.data
        print(data)        
        return Response({"data":data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        payload = {}
        data = request.data
        payload['bank_code'] = data.get('bank')
        payload['account_number'] = data.get('recipient')

        response = paystack_instance.resolve_account(payload)        
        return Response(response, status=status.HTTP_200_OK)
    
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