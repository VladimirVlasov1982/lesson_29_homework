from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ads.views import main_page
from ads.views.category import CategoriesViewSet
from homework_29 import settings
from users.views import LocationsViewSet

router = routers.SimpleRouter()
router.register("location", LocationsViewSet)
router.register("cat", CategoriesViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_page.main, name="main"),
    path("ad/", include("ads.urls.ad")),
    path("user/", include("users.urls")),
    path("", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
