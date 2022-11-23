import json
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from users.models import Users, Locations
from users.serializers import UsersListSerializer, UsersDetailSerializer, UsersCreateSerializer, UsersUpdateSerializer, \
    UsersDeleteSerializer, LocationsSerializer


class LocationsViewSet(ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer

class UsersListView(ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersListSerializer


    # model = Users
    #
    # def get(self, request, *args, **kwargs):
    #     """Получаем всех пользователей"""
    #     super().get(request, *args, **kwargs)
    #
    #     paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
    #     num_page = request.GET.get("page")
    #     page_obj = paginator.get_page(num_page)
    #
    #     users = []
    #     for user in page_obj:
    #         users.append({
    #             "id": user.id,
    #             "first_name": user.first_name,
    #             "last_name": user.last_name,
    #             "username": user.username,
    #             "role": user.role,
    #             "age": user.age,
    #             "locations": list(map(str, user.location_id.all())),
    #             "total_ads": user.ads.aggregate(num=Count("is_published", filter=Q(is_published=True)))["num"],
    #         })
    #
    #     return JsonResponse({
    #         "items": users,
    #         "num_pages": paginator.num_pages,
    #         "total": paginator.count,
    #     }, safe=False, json_dumps_params={"ensure_ascii": False})


class UsersDetailView(RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersDetailSerializer
    # model = Users
    #
    # def get(self, request, *args, **kwargs):
    #     """Получаем пользователя по id"""
    #     super().get(request, *args, **kwargs)
    #     self.object = self.get_object()
    #
    #     return JsonResponse({
    #         "id": self.object.id,
    #         "first_name": self.object.first_name,
    #         "last_name": self.object.last_name,
    #         "username": self.object.username,
    #         "role": self.object.role,
    #         "age": self.object.age,
    #         "locations": list(map(str, self.object.location_id.all())),
    #
    #     })



class UsersCreateView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersCreateSerializer
    # model = Users
    # fields = ["first_name", "last_name", "username", "password", "role", "age", "location_id"]
    #
    # def post(self, request, *args, **kwargs):
    #     """Создаем пользователя"""
    #     user_data = json.loads(request.body)
    #
    #     user = Users.objects.create(
    #         first_name=user_data["first_name"],
    #         last_name=user_data["last_name"],
    #         username=user_data["username"],
    #         password=user_data["password"],
    #         role=user_data["role"],
    #         age=user_data["age"],
    #     )
    #     if "locations" in user_data:
    #         for location in user_data["locations"]:
    #             location_obj, _ = Locations.objects.get_or_create(name=location)
    #             user.location_id.add(location_obj)
    #         user.save()
    #     return JsonResponse({
    #         "id": user.id,
    #         "first_name": user.first_name,
    #         "last_name": user.last_name,
    #         "username": user.username,
    #         "role": user.role,
    #         "age": user.age,
    #         "locations": list(map(str, user.location_id.all())),
    #
    #     })



class UsersUpdateView(UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersUpdateSerializer
    # model = Users
    # fields = ["first_name", "last_name", "username", "password", "age", "location_id"]
    #
    # def patch(self, request, *args, **kwargs):
    #     """Обновляем пользователя"""
    #     super().post(request, *args, **kwargs)
    #
    #     user_data = json.loads(request.body)
    #
    #     if "username" in user_data:
    #         self.object.username = user_data["username"]
    #     if "first_name" in user_data:
    #         self.object.first_name = user_data["first_name"]
    #     if "last_name" in user_data:
    #         self.object.last_name = user_data["last_name"]
    #     if "password" in user_data:
    #         self.object.password = user_data["password"]
    #     if "age" in user_data:
    #         self.object.age = user_data["age"]
    #     if "locations" in user_data:
    #         for location in user_data["locations"]:
    #             location_obj, _ = Locations.objects.get_or_create(name=location)
    #             self.object.location_id.add(location_obj)
    #
    #     self.object.save()
    #
    #     return JsonResponse({
    #         "id": self.object.id,
    #         "first_name": self.object.first_name,
    #         "last_name": self.object.last_name,
    #         "username": self.object.username,
    #         "age": self.object.age,
    #         "locations": list(map(str, self.object.location_id.all())),
    #
    #     })


class UsersDeleteView(DestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersDeleteSerializer

    # model = Users
    # success_url = "/"
    #
    # def delete(self, request, *args, **kwargs):
    #     """Удаляем пользователя"""
    #     super().delete(request, *args, **kwargs)
    #
    #     return JsonResponse({"status": "ok"}, status=200)

