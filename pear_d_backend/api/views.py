from rest_framework import generics
from rest_framework import response
from rest_framework.decorators import api_view
from .serializers import UserProfileSerializer
from .models import UserProfile

# Create your views here.

class UserProfileView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

