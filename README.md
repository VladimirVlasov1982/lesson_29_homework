# Урок 29. Сериализаторы и вьюсеты. Домашнее задание
***

#### Подготовка проекта Django

1. Установите docker-контейнер с уже готовой и настроенной СУБД:
```
docker run --name skypro-postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
```

2. Выполнить необходимые команды для подготовки базы данных к работе:
наполнение находится в фикстурах (папка fixtures).

Для начала нужно создать необходимые таблицы в базе данных с помощью команды:
python3 manage.py migrate.

А затем выполнить команды:

```
python manage.py loaddata fixtures/categories.json

python manage.py loaddata fixtures/locations.json

python manage.py loaddata fixtures/user.json

python manage.py loaddata fixtures/ads.json
```
Проект готов к работе.



