from django.urls import path
from .views import RestaurantView, UserProfileView

urlpatterns = [
    path('restaurants', RestaurantView.as_view()),
    path("profile/all", UserProfileView.as_view()),
]
