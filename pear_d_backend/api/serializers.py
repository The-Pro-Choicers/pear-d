from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserProfile, Restaurant
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


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "email",
            "prefer_price",
            "prefer_philanthropic",
            "prefer_env_conscious",
            "prefer_minority",
            "dark_mode",
            "favorites"
        )
