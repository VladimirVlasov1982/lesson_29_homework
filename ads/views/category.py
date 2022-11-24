from rest_framework.viewsets import ModelViewSet
from ads.models import Categories
from ads.serializers import CategoriesViewSerializer


class CategoriesViewSet(ModelViewSet):
    """Содержит в себе все базовые API-методы для категорий"""
    queryset = Categories.objects.all().order_by("name")
    serializer_class = CategoriesViewSerializer
