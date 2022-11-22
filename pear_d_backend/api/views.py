from django.shortcuts import render
from rest_framework import generics, mixins, permissions, authentication
# importing the restaurant serializer and its model
from .serializers import RestaurantSerializer
from .models import Restaurant

# Restaurant View
class RestaurantListAllView(generics.ListAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Restaurant.objects.all()
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
        return self.list(request, *args, **kwargs)


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
        if env_conscious_int is not None and philanthropic_int is not None and minority_int is not None and price_int is not None:
            qs = super().get_queryset().filter(
                price_level__exact=price_int,
                env_conscious__exact=bool(env_conscious_int),
                minority__exact=bool(minority_int),
                philanthropic__exact=bool(philanthropic_int),
                )
        # No env conscious
        elif philanthropic_int is not None and minority_int is not None and price_int is not None:
            qs = super().get_queryset().filter(
                price_level__exact=price_int,
                minority__exact=bool(minority_int),
                philanthropic__exact=bool(philanthropic_int),
                )
        else:
            qs = Restaurant.objects.none()
        return qs

        