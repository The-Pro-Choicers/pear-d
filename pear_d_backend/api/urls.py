from django.urls import path
from .views import RestaurantView

urlpatterns = [
    path('restaurants', RestaurantView.as_view())
]
