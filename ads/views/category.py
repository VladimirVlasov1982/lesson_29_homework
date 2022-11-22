import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from ads.models import Categories


class CategoriesListView(ListView):
    model = Categories

    def get(self, request, *args, **kwargs):
        """Получаем все категории"""
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by("name")

        response = []
        for category in self.object_list:
            response.append({
                "id": category.id,
                "name": category.name,
            })

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


class CategoriesDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        """Получаем категорию по id"""
        super().get(request, *args, **kwargs)
        category = self.get_object()

        return JsonResponse({
            "id": category.pk,
            "name": category.name,
        }, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class CategoriesCreateView(CreateView):
    model = Categories
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        """Создаем категорию"""
        categories_data = json.loads(request.body)
        category = Categories.objects.create(
            name=categories_data["name"],
        )
        return JsonResponse({
            "id": category.id,
            "name": category.name,
        }, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class CategoriesUpdateView(UpdateView):
    model = Categories
    fields = ["name"]

    def patch(self, request, *args, **kwargs):
        """Обновляем категорию"""
        super().post(request, *args, **kwargs)

        cat_data = json.loads(request.body)

        if "name" in cat_data:
            self.object.name = cat_data["name"]

        self.object.save()

        return JsonResponse({
            "id": self.object.pk,
            "name": self.object.name,
        })


@method_decorator(csrf_exempt, name="dispatch")
class CategoriesDeleteView(DeleteView):
    model = Categories
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        """Удаляем категорию"""
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"})
