from rest_framework import serializers
from ads.models import Ads, Categories
from users.models import Users


class CategoriesViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class AdsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = "__all__"


class AdsDetailSeraializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
        source="author_id"
    )
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name",
        source="category_id"
    )

    class Meta:
        model = Ads
        exclude = ["author_id", "category_id"]


class AdsCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    author_id = serializers.SlugRelatedField(
        required=False,
        queryset=Users.objects.all(),
        slug_field="pk",
    )
    category_id = serializers.SlugRelatedField(
        required=False,
        queryset=Categories.objects.all(),
        slug_field="pk",
    )

    class Meta:
        model = Ads
        fields = "__all__"


class AdsUpdateSerializer(serializers.ModelSerializer):
    author_id = serializers.SlugRelatedField(
        required=False,
        queryset=Users.objects.all(),
        slug_field="pk"
    )
    category_id = serializers.SlugRelatedField(
        required=False,
        queryset=Categories.objects.all(),
        slug_field="pk"
    )

    class Meta:
        model = Ads
        fields = "__all__"


class AdsDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ["id"]
