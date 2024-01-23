from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.api.urls')),
    path('home/', include('apps.crypto_world.urls')),
    path('account/', include('apps.accounts.urls')),
    path('admin/', admin.site.urls),
]