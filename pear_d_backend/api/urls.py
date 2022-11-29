from django.urls import path
from .views import RestaurantListAllView, RestaurantDetailedView, FindRestaurantView, UserAccountAllView, UserAccountUpdateView, UserAccountRetrieveView, FavoritesUpdateView, UserFavoritesDeleteView

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
    path("profile/admin/all/", UserAccountAllView.as_view()),
    path("profile/myprofile/update/", UserAccountUpdateView.as_view()),
    path("profile/myprofile/view/", UserAccountRetrieveView.as_view()),
    path("profile/myprofile/favorites/add/", FavoritesUpdateView.as_view()),
    path("profile/myprofile/favorites/delete/<int:id>/", UserFavoritesDeleteView.as_view()),
]
