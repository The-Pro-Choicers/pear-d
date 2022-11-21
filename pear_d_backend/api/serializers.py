from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Restaurant
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