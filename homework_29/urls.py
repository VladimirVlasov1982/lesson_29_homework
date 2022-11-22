from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ads.views import main_page
from homework_29 import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_page.main, name="main"),
    path("ad/", include("ads.urls.ad")),
    path("cat/", include("ads.urls.category")),
    path("user/", include("users.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
