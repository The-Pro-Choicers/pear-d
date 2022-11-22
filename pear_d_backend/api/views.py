from rest_framework import generics
from rest_framework import respons
from rest_framework.decorators import api_view
from .serializers import UserProfileSerializer, RestaurantSerializer
from .models import UserProfile, Restaurant

# Restaurant View
class RestaurantView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class UserProfileView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

