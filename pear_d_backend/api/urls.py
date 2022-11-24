from django.urls import path
from .views import RestaurantView, UserAccountView

urlpatterns = [
    path('restaurants', RestaurantView.as_view()),
    path("profile/all/", UserAccountView.as_view()),
]
