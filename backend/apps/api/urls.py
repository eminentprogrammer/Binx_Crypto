from django.urls import path
from . import views

urlpatterns = [
    path('', views.api, name="api"),
    path("buy_data/", views.buy_data, name="buy_data"),
    path("make_transfer/", views.make_transfer, name="make_transfer"),
    path("get_banks/", views.get_banks, name="get_banks"),
]
