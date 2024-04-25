from django.urls import path
from .views import *

urlpatterns = [
    path('', api, name="api"),
    path("buy_data/", buy_data.as_view(), name="buy_data"),
    path("make_transfer/", make_transfer.as_view(), name="make_transfer"),
    path("banks/", listBanks.as_view(), name="listBanks"),
    path('complete_transfer/', complete_transfer.as_view(), name="complete_transfer"),
    path("transfer/<str:transaction_id>/", getTransaction.as_view(), name="getTransaction"),
]