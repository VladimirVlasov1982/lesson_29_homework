from django.db import models
from users.models import Users


# Модель категории
class Categories(models.Model):
    name = models.CharField(max_length=300)

    objects = models.Manager()

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


# Модель объявления
class Ads(models.Model):
    name = models.CharField(max_length=200)
    author_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="ads", null=True)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    is_published = models.BooleanField()
    image = models.ImageField(upload_to="pictures", null=True, blank=True)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name
