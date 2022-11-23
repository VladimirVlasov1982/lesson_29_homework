from rest_framework import serializers

from ads.models import Ads
from users.models import Users, Locations


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ["is_published"]

class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'


class UsersListSerializer(serializers.ModelSerializer):
    location_id = LocationsSerializer(many=True)
    # location_id = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field="name",
    # )
    ads = serializers.SlugRelatedField(
        many=True,
        queryset=Ads.objects.all().filter(is_published=True).count(),
        slug_field="name",
    )
    class Meta:
        model = Users
        fields = ["id", "first_name", "last_name", "username", "role", "age", "location_id", "ads"]


class UsersDetailSerializer(serializers.ModelSerializer):
    location_id = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
    )
    class Meta:
        model = Users
        fields = ["id", "first_name", "last_name", "username", "role", "age", "location_id"]


class UsersCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    location_id = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Locations.objects.all(),
        slug_field="name"
    )
    class Meta:
        model = Users
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop("locations")

        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user =Users.objects.create(**validated_data)

        for location in self._locations:
            location_obj, _ = Locations.objects.get_or_create(name=location)
            user.location_id.add(location_obj)
        user.save()

        return user

class UsersUpdateSerializer(serializers.ModelSerializer):
    location_id = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Locations.objects.all(),
        slug_field="name"
    )
    class Meta:
        model = Users
        exclude = ["password"]

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop("locations")
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        user = super().save()

        for location in self._locations:
            location_obj, _ = Locations.objects.get_or_create(name=location)
            user.location_id.add(location_obj)

        user.save()
        return user

class UsersDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["id"]
