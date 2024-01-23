from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage_view, name="homepage"),
    path('transfer/', views.send, name='send'),
    path("buy-data/", views.buy_data, name="data"),
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
]
