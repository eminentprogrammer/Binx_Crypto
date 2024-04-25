import json
import requests
from .auth import *
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.paystack.utils import load_lib
from apps.finance.models import Transfer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, permissions, status


# PAYSTACK
PayStackAPI = load_lib()
paystack_instance = PayStackAPI()


def api(request):
    response = {
        'status'    : 'success',
        'server'    : 'Binx Crypto',
        'message'   : 'API is Live',
    }
    return JsonResponse(response, safe=False)


class listBanks(APIView):
    permission_classes = [permissions.AllowAny]    
    def get(self, request, format=None):
        banks = paystack_instance.list_banks()
        return JsonResponse(banks, safe=False)


class make_transfer(APIView):
    permission_classes = [permissions.AllowAny]    
    def get(self, request, format=None):
        return Response({"message":"Invalid Request"}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        payload = {}
        payload['bank_code'] = request.data.get('bank')
        payload['account_number'] = request.data.get('recipient')
        
        response = paystack_instance.resolve_account(payload)
        # if response[0]:
        #     transfer_instance = Transfer.objects.create(
        #         recipient_name=response[2]['account_name'],
        #         recipient_account=response[2]['account_number'],
        #         recipient_bank = data.get('bank'),
        #     )
        #     transfer_instance.save()
        response[2]['transfer_id'] = "transfer_instance.id"
        return Response(response, status=status.HTTP_200_OK)



class buy_data(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, format=None):        
        data            = request.data
        phone           = data['recipient']
        plan            = data['plan']
        network         = data['network']
        print(data)
        
        TOKEN           = SME_TOKEN    
        url             = f"https://smedata.ng/wp-json/api/v1/data?token={TOKEN}&network={network}&phone={phone}&size={plan}"
        response        = requests.get(url=url, headers=SME_HEADERS).json()
        
        if response['code'] == "success":
            response_data   = {
                "status": True,
                "data" : response["data"],
                "message": response['message']
            }
            return JsonResponse(response_data, safe=True)       
        else:
            response_data = {
                "status"    : "404",
                "message"   : response["message"]
            }        
        return JsonResponse(response_data, safe=False)
    

class complete_transfer(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request, format=None):
        data = request.data
        pin = data.get('pin')
        transaction_instance = data.get('transfer_id')
        
        print(data)
        if pin == "1234":
            return JsonResponse({"status": True, "message":"Pin Verified"})
        else:
            return JsonResponse({"status":"failed", "message":"Pin Invalid"})
        

class getTransaction(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, transaction_id, format=None):
        print(transaction_id)
        # transaction_instance = Transfer.objects.get(id=transaction_id)
        
        return redirect("/home/")