from django.shortcuts import render

def homepage_view(request):
    return render(request, 'homepage.html')

def send(request):
    return render(request, 'savings/make_transfer.html')

def deposit(request):
    pass

def withdraw(request):
    pass

def buy_data(request):

    return render(request, 'savings/buy_data.html')