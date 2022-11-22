from django.urls import path
from users.views import UsersListView, UsersDetailView, UsersCreateView, UsersUpdateView, UsersDeleteView

urlpatterns = [
    path("", UsersListView.as_view(), name="user"),
    path("<int:pk>/", UsersDetailView.as_view(), name="user-detail"),
    path("create/", UsersCreateView.as_view(), name="user-create"),
    path("<int:pk>/update/", UsersUpdateView.as_view(), name="user-update"),
    path("<int:pk>/delete/", UsersDeleteView.as_view(), name="user-delete"),
]
