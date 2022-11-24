from django.urls import path
from .views import RestaurantView, UserAccountAllView, UserAccountUpdateView, UserAccountRetrieveView, FavoritesUpdateView, UserFavoritesDeleteView

urlpatterns = [
    path('restaurants', RestaurantView.as_view()),
    path("profile/admin/all/", UserAccountAllView.as_view()),
    path("profile/myprofile/update/", UserAccountUpdateView.as_view()),
    path("profile/myprofile/view/", UserAccountRetrieveView.as_view()),
    path("profile/myprofile/favorites/add/", FavoritesUpdateView.as_view()),
    path("profile/myprofile/favorites/delete/<int:id>/", UserFavoritesDeleteView.as_view()),
]
