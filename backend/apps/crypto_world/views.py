import os
import environ
from pathlib import Path
from django.shortcuts import render


env = environ.Env(DEBUG=(bool, False))
BASE_DIR = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

def homepage_view(request):
    return render(request, 'homepage.html')

def send(request):
    context = {}
    context['token'] = env('PAYSTACK_TEST_KEY')
    return render(request, 'savings/make_transfer.html', context)

def deposit(request):
    pass

def withdraw(request):
    pass

def buy_data(request):

    return render(request, 'savings/buy_data.html')