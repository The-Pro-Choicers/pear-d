from django.urls import path
from .views import RestaurantListAllView, RestaurantDetailedView, FindRestaurantView, UserAccountAllView, UserAccountUpdateView, UserAccountRetrieveView, FavoritesUpdateView, UserFavoritesDeleteView

urlpatterns = [
    path('restaurants/all', RestaurantListAllView.as_view()),
    path("restaurants/<int:id>/", RestaurantDetailedView.as_view()),
    path("restaurants/pl=<int:price>env=<int:env_conscious>ph=<int:philanthropic>m=<int:minority>/", FindRestaurantView.as_view()),
    path("restaurants/pl=<int:price>ph=<int:philanthropic>m=<int:minority>/", FindRestaurantView.as_view()),
    path("profile/admin/all/", UserAccountAllView.as_view()),
    path("profile/myprofile/update/", UserAccountUpdateView.as_view()),
    path("profile/myprofile/view/", UserAccountRetrieveView.as_view()),
    path("profile/myprofile/favorites/add/", FavoritesUpdateView.as_view()),
    path("profile/myprofile/favorites/delete/<int:id>/", UserFavoritesDeleteView.as_view()),
]
