from django.urls import path

from .views import BeerListView, BeerDetailView


urlpatterns = [
    path("", BeerListView.as_view(), name="beer_list"),
    path("<uuid:pk>/", BeerDetailView.as_view(), name="beer_detail"),
]