from rest_framework import generics, response, mixins, permissions, authentication
from rest_framework.decorators import api_view
from .serializers import UserAccountSerializer, RestaurantSerializer, FavoritesSerializer
from .models import UserAccount, Restaurant, Favorites
from django.shortcuts import get_object_or_404
from django.db.models.functions import Cast
from django.db.models.expressions import Func


# Restaurant View
class RestaurantListAllView(generics.ListAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Restaurant.objects.all().order_by("-rating")
    serializer_class = RestaurantSerializer


class RestaurantDetailedView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Restaurant.objects.all()
    serializer_class=RestaurantSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return self.retrieve(request, *args, **kwargs)
        return Restaurant.objects.none()


class FindRestaurantView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        

    def get_queryset(self):
        kwargs = self.kwargs
        print(kwargs)
        env_conscious_int = kwargs.get("env_conscious")
        philanthropic_int = kwargs.get("philanthropic")
        minority_int = kwargs.get("minority")
        price_int = kwargs.get("price")

        # Input validation
        if env_conscious_int is not None:
            if env_conscious_int > 1 or env_conscious_int < 0:
                env_conscious_int = 0
        
        if philanthropic_int is not None:
            if philanthropic_int > 1 or philanthropic_int < 0:
                philanthropic_int = 0
        
        if minority_int is not None:
            if minority_int > 1 or minority_int < 0:
                minority_int = 0

        qs = None
        # Conditionals for whether we are filtering each of the social filters or not
        # env + phil + min + price
        if env_conscious_int is not None and philanthropic_int is not None and minority_int is not None and price_int is not None:
            qs = super().get_queryset().filter(
                price_level__exact=price_int,
                env_conscious__exact=bool(env_conscious_int),
                minority__exact=bool(minority_int),
                philanthropic__exact=bool(philanthropic_int),
                )
        # phil + min + price
        elif philanthropic_int is not None and minority_int is not None and price_int is not None:
            qs = super().get_queryset().filter(
                price_level__exact=price_int,
                minority__exact=bool(minority_int),
                philanthropic__exact=bool(philanthropic_int),
                )
        # env + min + price
        elif env_conscious_int is not None and minority_int is not None and price_int is not None:
            qs = super().get_queryset().filter(
                price_level__exact=price_int,
                env_conscious__exact=bool(env_conscious_int),
                minority__exact=bool(minority_int),
                )
        # env + phil + price
        elif env_conscious_int is not None and philanthropic_int is not None and price_int is not None:
            qs = super().get_queryset().filter(
                price_level__exact=price_int,
                env_conscious__exact=bool(env_conscious_int),
                philanthropic__exact=bool(philanthropic_int),
                )
        # env + phil + min
        elif env_conscious_int is not None and philanthropic_int is not None and minority_int is not None:
            qs = super().get_queryset().filter(
                env_conscious__exact=bool(env_conscious_int),
                minority__exact=bool(minority_int),
                philanthropic__exact=bool(philanthropic_int),
                )
        # env + phil
        elif env_conscious_int is not None and philanthropic_int is not None:
            qs = super().get_queryset().filter(
                env_conscious__exact=bool(env_conscious_int),
                philanthropic__exact=bool(philanthropic_int),
                )
        # env + min
        elif env_conscious_int is not None and minority_int is not None:
            qs = super().get_queryset().filter(
                env_conscious__exact=bool(env_conscious_int),
                minority__exact=bool(minority_int),
                )
        # env + price
        elif env_conscious_int is not None and price_int is not None:
            qs = super().get_queryset().filter(
                price_level__exact=price_int,
                env_conscious__exact=bool(env_conscious_int),
                )
        # phil + min
        elif philanthropic_int is not None and minority_int is not None:
            qs = super().get_queryset().filter(
                minority__exact=bool(minority_int),
                philanthropic__exact=bool(philanthropic_int),
                )
        # phil + price
        elif philanthropic_int is not None and price_int is not None:
            qs = super().get_queryset().filter(
                price_level__exact=price_int,
                philanthropic__exact=bool(philanthropic_int),
                )
        # min + price
        elif minority_int is not None and price_int is not None:
            qs = super().get_queryset().filter(
                price_level__exact=price_int,
                minority__exact=bool(minority_int),
                )
        # env only
        elif env_conscious_int is not None:
            qs = super().get_queryset().filter(
                env_conscious__exact=bool(env_conscious_int),
                )
        # phil only
        elif philanthropic_int is not None:
            qs = super().get_queryset().filter(
                philanthropic__exact=bool(philanthropic_int),
                )
        # min only
        elif minority_int is not None:
            qs = super().get_queryset().filter(
                minority__exact=bool(minority_int),
                )
        # price only
        elif price_int is not None:
            qs = super().get_queryset().filter(
                price_level__exact=price_int,
                )
        # no filter so return all
        else:
            qs = super().get_queryset()
        return qs.order_by("-rating")

        
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
        