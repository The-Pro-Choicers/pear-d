from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserAccount, Restaurant, Favorites

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password')


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
                'id', # on each model, there is a "primary key" - this is it
                'name',
                'address',
                'photo_ref',
                'price_level',
                'rating',
                'url',
                'env_conscious',
                'minority',
                'philanthropic')


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = (
            "restaurant_id",
        )

    def validate(self, data):
        if data.get("restaurant_id") is not None:
            if data['restaurant_id'] < 0:
                raise serializers.ValidationError("Invalid restaurant id")
        return data


class UserAccountSerializer(serializers.ModelSerializer):
    favorites = FavoritesSerializer(many=True, read_only=True)

    class Meta:
        model = UserAccount
        fields = (
            "email",
            "name",
            "prefer_price",
            "prefer_philanthropic",
            "prefer_env_conscious",
            "prefer_minority",
            "dark_mode",
            "favorites",
        )
        read_only_fields = ("email", "favorites")
    
    def validate(self, data):
        if data.get("prefer_price") is not None:
            if data['prefer_price'] > 4 or data["prefer_price"] < 1:
                raise serializers.ValidationError("Invalid price level")
        return data


