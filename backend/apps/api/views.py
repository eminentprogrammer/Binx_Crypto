import json
from django.shortcuts import render
from django.http import JsonResponse


def api(request):
    response_data = {
        'status'    : 'success',
        'server'    : 'Binx Crypto',
        'message'   : 'API is Live',
    }
    return JsonResponse(response_data, safe=False)