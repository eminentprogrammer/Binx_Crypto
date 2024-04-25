from django.urls import path
from .views import *

urlpatterns = [
    path('', api, name="api"),
    path("buy_data/", buy_data, name="buy_data"),
    path("make_transfer/", make_transfer.as_view(), name="make_transfer"),
    path("banks/", listBanks.as_view(), name="listBanks"),
]