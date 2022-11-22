import json
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from ads.models import Categories, Ads
from homework_29.settings import TOTAL_ON_PAGE
from users.models import Users


class AdsListView(ListView):
    model = Ads

    def get(self, request, *args, **kwargs):
        """Получаем все объявления"""
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.select_related("author_id").select_related("category_id").order_by("-price")

        paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
        num_page = request.GET.get("page")
        page_obj = paginator.get_page(num_page)

        ads = []

        for ad in page_obj:
            ads.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author_id.username,
                "category": ad.category_id.name,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "image": ad.image.url if ad.image else None,
            })

        response = {
            "item": ads,
            "num_pages": paginator.num_pages,
            "total": paginator.count,
        }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        """Получаем объявление по id"""
        super().get(request, *args, **kwargs)
        ad = self.get_object()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author_id.username,
            "category": ad.category_id.name,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "image": ad.image.url if ad.image else None
        }, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdsCreateView(CreateView):
    model = Ads
    fields = ["name", "author_id", "price", "description", "is_published", "category_id"]

    def post(self, request, *args, **kwargs):
        """Создаем объявление"""
        ads_data = json.loads(request.body)

        author = get_object_or_404(Users, pk=ads_data["author_id"])
        category = get_object_or_404(Categories, pk=ads_data["category_id"])

        ad = Ads.objects.create(
            name=ads_data["name"],
            author_id=author,
            price=ads_data["price"],
            description=ads_data["description"],
            is_published=ads_data["is_published"],
            category_id=category,
        )
        return JsonResponse({
            "id": ad.pk,
            "name": ad.name,
            "author": author.username,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "category": category.name,
        })


@method_decorator(csrf_exempt, name="dispatch")
class AdsUpdateView(UpdateView):
    model = Ads
    fields = ["name", "author_id", "price", "description", "category_id"]

    def patch(self, request, *args, **kwargs):
        """Обновляем объявление"""
        super().post(request, *args, **kwargs)

        ads_data = json.loads(request.body)

        if "name" in ads_data:
            self.object.name = ads_data["name"]
        if "author_id" in ads_data:
            author = get_object_or_404(Users, pk=ads_data["author_id"])
            self.object.author_id = author
        if "price" in ads_data:
            self.object.price = ads_data["price"]
        if "description" in ads_data:
            self.object.description = ads_data["description"]
        if "category_id" in ads_data:
            category = get_object_or_404(Categories, pk=ads_data["category_id"])
            self.object.category_id = category

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author_id.username,
            "category": self.object.category_id.name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image.url if self.object.image else None
        }, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdsDeleteView(DeleteView):
    model = Ads
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        """Удаляем объявление"""
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "Ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AdsUploadImage(UpdateView):
    model = Ads
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        """Загружаем картинку для объявления"""
        super().post(request, *args, **kwargs)
        self.object = self.get_object()
        self.object.image = request.FILES.get("image")
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author_id.username,
            "category": self.object.category_id.name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image.url if self.object.image else None
        }, json_dumps_params={"ensure_ascii": False})
