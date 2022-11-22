from django.db import models


# Модель локации
class Locations(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


# Модель пользователь
class Users(models.Model):
    ROLES = [
        ("member", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Администратор"),
    ]

    first_name = models.CharField(max_length=100, verbose_name="Имя", null=True)
    last_name = models.CharField(max_length=100, verbose_name="Фамилия", null=True)
    username = models.CharField(max_length=100, verbose_name="Логин", unique=True)
    password = models.CharField(max_length=50, verbose_name="Пароль")
    role = models.CharField(max_length=10, choices=ROLES, default="member")
    age = models.SmallIntegerField()
    location_id = models.ManyToManyField(Locations)

    objects = models.Manager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
