from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('apps.api.urls')),
    path('home/', include('apps.crypto_world.urls')),
    path('account/', include('apps.accounts.api.urls')),
    path('admin/', admin.site.urls),
    path('health/', include('health_check.urls', namespace='health')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)