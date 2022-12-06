from django.urls import path, re_path
from .views import RestaurantListAllView, RestaurantDetailedView, FindRestaurantView, UserAccountAllView, UserAccountUpdateView, UserAccountRetrieveView, FavoritesUpdateView, UserFavoritesDeleteView

urlpatterns = [
    # URLS for Restaurant
    # EVERYTHING IN HERE IS PRECEDED BY /api/
    # Format for filtered endpoint is /fc[int]e[int]ph[int]m[int]p[int]
    re_path(r'^restaurants/filter/(((fc)(?P<food_category>\d))?((e)(?P<env_conscious>\d))?((ph)(?P<philanthropic>\d))?((m)(?P<minority>\d))?((p)(?P<price>\d))?/)?$', FindRestaurantView.as_view()),
    path('restaurants/all', RestaurantListAllView.as_view()),
    path("restaurants/detailed/<int:id>/", RestaurantDetailedView.as_view()),
    # URLS for User Account Profiles
    path("profile/admin/all/", UserAccountAllView.as_view()),
    path("profile/myprofile/update/", UserAccountUpdateView.as_view()),
    path("profile/myprofile/view/", UserAccountRetrieveView.as_view()),
    path("profile/myprofile/favorites/delete/<int:id>/", UserFavoritesDeleteView.as_view()),
    path("profile/myprofile/favorites/add/", FavoritesUpdateView.as_view()),
    
]
