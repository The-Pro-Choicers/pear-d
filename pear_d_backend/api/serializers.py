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
    # Returning custom version of the data so that it can be printed out better visually
    price_level = serializers.SerializerMethodField()
    food_category = serializers.SerializerMethodField()
    env_conscious = serializers.SerializerMethodField()
    minority = serializers.SerializerMethodField()
    philanthropic = serializers.SerializerMethodField()
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
                'philanthropic',
                'food_category'
        )

    
    def get_philanthropic(self, obj):
        if obj.philanthropic is True:
            return "Philanthropic"
        else:
            return ""


    def get_env_conscious(self, obj):
        if obj.env_conscious is True:
            return "Environmentally Friendly"
        else:
            return ""

    
    def get_minority(self, obj):
        if obj.minority is True:
            return "Minority Owned"
        else:
            return ""

    
    def get_food_category(self, obj):
        if obj.food_category == 0:
            return "Fast Food / Chain"
        elif obj.food_category == 1:
            return "Drinks/Desert"
        elif obj.food_category == 2:
            return "American"
        elif obj.food_category == 3:
            return "Asian"
        elif obj.food_category == 4:
            return "Hispanic"
        elif obj.food_category == 5:
            return "Indian"
        elif obj.food_category == 6:
            return "Italian"
        elif obj.food_category == 7:
            return "Mediterranean"
        elif obj.food_category == 8:
            return "Seafood"
        else:
            return "Unknown"
    

    def get_price_level(self, obj):
        if obj.price_level == 1:
            return "$"
        elif obj.price_level == 2:
            return "$$"
        elif obj.price_level == 3:
            return "$$$"
        elif obj.price_level == 4:
            return "$$$$"
        else:
            return "Unknown"


class FavoritesSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    class Meta:
        model = Favorites
        fields = (
            "restaurant",
        )
        read_only_fields = ("restaurant",)

    def validate(self, data):
        if data.get("restaurant_id") is not None and data['restaurant_id'] < 0:
            raise serializers.ValidationError("Invalid restaurant id")
        return data


class UserAccountSerializer(serializers.ModelSerializer):
    favorites = FavoritesSerializer(many=True, read_only=True)
    prefer_price = serializers.SerializerMethodField()
    prefer_philanthropic = serializers.SerializerMethodField()
    prefer_env_conscious = serializers.SerializerMethodField()
    prefer_minority = serializers.SerializerMethodField()

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


    def get_prefer_price(self, obj):
        if obj.prefer_price == 1:
            return "$"
        elif obj.prefer_price == 2:
            return "$$"
        elif obj.prefer_price == 3:
            return "$$$"
        elif obj.prefer_price == 4:
            return "$$$$"
        else:
            return "Unknown"


    def get_prefer_philanthropic(self, obj):
        if obj.prefer_philanthropic == 1:
            return "Restaurants that are philanthropic"
        else:
            return ""


    def get_prefer_env_conscious(self, obj):
        if obj.prefer_env_conscious == 1:
            return "Restaurants that care about the environment"
        else:
            return ""


    def get_prefer_minority(self, obj):
        if obj.prefer_minority == 1:
            return "Minority-owned restaurants"
        else:
            return ""
    


