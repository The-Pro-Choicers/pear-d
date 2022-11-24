from rest_framework import generics, response, mixins, permissions, authentication
from rest_framework.decorators import api_view
from .serializers import UserAccountSerializer, RestaurantSerializer, FavoritesSerializer
from .models import UserAccount, Restaurant, Favorites
from django.shortcuts import get_object_or_404
from django.db.models.functions import Cast
from django.db.models.expressions import Func


# Restaurant View
class RestaurantView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser,]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class UserAccountAllView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser,]
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

class UserAccountUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"detail": "1"})
        else:
            return response.Response({"detail": "0"})

    def get_object(self):
        return get_object_or_404(UserAccount, pk=self.request.user)
        

class UserAccountRetrieveView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = UserAccount.objects.all()
    serializer_class=UserAccountSerializer

    # Overloaded get_object to filter just this current user's account from DB
    def get_object(self):
        return get_object_or_404(UserAccount, pk=self.request.user)

# Used for Adding new Favorite
class FavoritesUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer

    def update(self, request, *args,**kwargs):
        rest_id = request.data.get("restaurant_id")
        if not Restaurant.objects.filter(id=rest_id):
            return response.Response({"exit_code": "1"})
        else:
            Favorites.objects.all().filter(user_email = request.user).update_or_create(
                user_email=request.user,
                restaurant_id=rest_id,
                defaults={
                    "user_email": request.user,
                    "restaurant_id" : rest_id,
                }
            )
            return response.Response({"exit_code": "0"})


class UserFavoritesDeleteView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
    
    def get(self, request, *args,**kwargs):
        obj = Favorites.objects.filter(user_email=request.user, restaurant_id=kwargs.get("id"))
        if not obj:
            return response.Response({"exit_code": "1"})
        else:
            obj.delete()
            return response.Response({"exit_code": "0"})
        