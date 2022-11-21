from django.shortcuts import render
from rest_framework import generics
# importing the restaurant serializer and its model
from .serializers import RestaurantSerializer
from .models import Restaurant

# Restaurant View
class RestaurantView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
