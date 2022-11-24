from rest_framework import generics, response, mixins, permissions, authentication
from rest_framework.decorators import api_view
from .serializers import UserAccountSerializer, RestaurantSerializer
from .models import UserAccount, Restaurant

# Restaurant View
class RestaurantView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class UserAccountView(generics.CreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

