from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("nft_market.api.urls")),
    path("health/", lambda request: HttpResponse(status=200)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if  settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
