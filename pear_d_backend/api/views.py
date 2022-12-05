from rest_framework import generics, response, mixins, permissions, authentication, renderers
from .serializers import UserAccountSerializer, RestaurantSerializer, FavoritesSerializer
from .models import UserAccount, Restaurant, Favorites
from django.shortcuts import get_object_or_404

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
    renderer_classes = [renderers.JSONRenderer]
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
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
    renderer_classes = [renderers.JSONRenderer]
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        

    def get_queryset(self):
        kwargs = self.kwargs
        env_conscious_int = philanthropic_int = minority_int = price_int = food_category_int = None
        if kwargs.get("food_category") is not None:
            food_category_int = int(kwargs.get("food_category"))
        if kwargs.get("env_conscious") is not None:
            env_conscious_int = int(kwargs.get("env_conscious"))
        if kwargs.get("philanthropic") is not None:
            philanthropic_int = int(kwargs.get("philanthropic"))
        if kwargs.get("minority") is not None:
            minority_int = int(kwargs.get("minority"))
        if kwargs.get("price") is not None:
            price_int = int(kwargs.get("price"))

        # Input validation
        if food_category_int is not None:
            if food_category_int < 0 or food_category_int > 6:
                food_category_int = 0

        if env_conscious_int is not None:
            if env_conscious_int > 1 or env_conscious_int < 0:
                env_conscious_int = 0
        
        if philanthropic_int is not None:
            if philanthropic_int > 1 or philanthropic_int < 0:
                philanthropic_int = 0

        if minority_int is not None:
            if minority_int > 1 or minority_int < 0:
                minority_int = 0

        qs = super().get_queryset()
        # Conditionals for whether we are filtering each of the social filters or not
        if food_category_int is not None:
            qs = qs.filter(food_category=food_category_int)

        if env_conscious_int is not None:
            qs = qs.filter(
                env_conscious__exact=bool(env_conscious_int),
            )

        if philanthropic_int is not None:
            qs = qs.filter(
                philanthropic__exact=bool(philanthropic_int),
            )

        if minority_int is not None:
            qs = qs.filter(
                minority__exact=bool(minority_int),
            )

        if price_int is not None:
            qs = qs.filter(
                price_level__exact=price_int,
            )
        
        return qs.order_by("-rating")

        
class UserAccountAllView(generics.ListAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer


class UserAccountUpdateView(generics.UpdateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [permissions.IsAuthenticated]
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
    authentication_classes = [authentication.SessionAuthentication]
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserAccount.objects.all()
    serializer_class=UserAccountSerializer

    # Overloaded get_object to filter just this current user's account from DB
    def get_object(self):
        return get_object_or_404(UserAccount, pk=self.request.user)

# Used for Adding new Favorite
class FavoritesUpdateView(generics.UpdateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [permissions.IsAuthenticated]
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
    authentication_classes = [authentication.SessionAuthentication]
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
    
    def get(self, request, *args,**kwargs):
        obj = Favorites.objects.filter(user_email=request.user, restaurant_id=kwargs.get("id"))
        if not obj:
            return response.Response({"exit_code": "1"})
        else:
            obj.delete()
            return response.Response({"exit_code": "0"})
        