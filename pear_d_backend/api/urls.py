from django.urls import path
from .views import RestaurantListAllView, RestaurantDetailedView, FindRestaurantView

urlpatterns = [
    path('restaurants/all', RestaurantListAllView.as_view()),
    path("restaurants/detailed/<int:id>/", RestaurantDetailedView.as_view()),
    path("restaurants/socialfilter/e=<int:env_conscious>ph=<int:philanthropic>m=<int:minority>p=<int:price>/", FindRestaurantView.as_view()),
    path("restaurants/socialfilter/ph=<int:philanthropic>m=<int:minority>p=<int:price>/", FindRestaurantView.as_view()),
    path("restaurants/socialfilter/e=<int:env_conscious>m=<int:minority>p=<int:price>/", FindRestaurantView.as_view()),
    path("restaurants/socialfilter/e=<int:env_conscious>ph=<int:philanthropic>p=<int:price>/", FindRestaurantView.as_view()),
    path("restaurants/socialfilter/e=<int:env_conscious>ph=<int:philanthropic>m=<int:minority>/", FindRestaurantView.as_view()),
    path("restaurants/socialfilter/e=<int:env_conscious>ph=<int:philanthropic>/", FindRestaurantView.as_view()),
    path("restaurants/socialfilter/e=<int:env_conscious>m=<int:minority>/", FindRestaurantView.as_view()),
    path("restaurants/socialfilter/e=<int:env_conscious>p=<int:price>/", FindRestaurantView.as_view()),
    path("restaurants/socialfilter/ph=<int:philanthropic>m=<int:minority>/", FindRestaurantView.as_view()),
    path("restaurants/socialfilter/ph=<int:philanthropic>p=<int:price>/", FindRestaurantView.as_view()),
    path("restaurants/socialfilter/m=<int:minority>p=<int:price>/", FindRestaurantView.as_view()),
    path("restaurants/socialfilter/e=<int:env_conscious>/", FindRestaurantView.as_view()),
    path("restaurants/socialfilter/ph=<int:philanthropic>/", FindRestaurantView.as_view()),
    path("restaurants/socialfilter/m=<int:minority>/", FindRestaurantView.as_view()),
    path("restaurants/socialfilter/p=<int:price>/", FindRestaurantView.as_view()),
]
