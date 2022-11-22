from django.urls import path
from ads.views.category import CategoriesListView, CategoriesDetailView, CategoriesCreateView, CategoriesUpdateView, \
    CategoriesDeleteView

urlpatterns = [
    path("", CategoriesListView.as_view(), name="categories"),
    path("<int:pk>/", CategoriesDetailView.as_view(), name="categories-detail"),
    path("create/", CategoriesCreateView.as_view(), name="categories-create"),
    path("<int:pk>/update/", CategoriesUpdateView.as_view(), name="categories-update"),
    path("<int:pk>/delete/", CategoriesDeleteView.as_view(), name="categories-delete"),
]
