from django.urls import path
from .views import RestaurantListAllView, RestaurantDetailedView, FindRestaurantView

urlpatterns = [
    path('restaurants/all', RestaurantListAllView.as_view()),
    path("restaurants/<int:id>/", RestaurantDetailedView.as_view()),
    path("restaurants/pl=<int:price>env=<int:env_conscious>ph=<int:philanthropic>m=<int:minority>/", FindRestaurantView.as_view()),
    path("restaurants/pl=<int:price>ph=<int:philanthropic>m=<int:minority>/", FindRestaurantView.as_view())
]
