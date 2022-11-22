from rest_framework import generics
from rest_framework import response
from rest_framework.decorators import api_view
from .serializers import UserProfileSerializer
from .models import UserProfile
# importing the restaurant serializer and its model
from .serializers import RestaurantSerializer
from .models import Restaurant

# Restaurant View
class RestaurantView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class UserProfileView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

