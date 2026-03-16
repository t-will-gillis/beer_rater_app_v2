from django.urls import path

from .views import (
    BeerListView,
    BeerDetailView,
    BeerCreateView,
    BeerUpdateView,
    BeerDeleteView,
    SearchResultsListView,
)


urlpatterns = [
    path("", BeerListView.as_view(), name="beer_list"),
    path("<uuid:pk>/", BeerDetailView.as_view(), name="beer_detail"),
    path("add/", BeerCreateView.as_view(), name="beer_create"),
    path("<uuid:pk>/edit/", BeerUpdateView.as_view(), name="beer_update"),
    path("<uuid:pk>/delete/", BeerDeleteView.as_view(), name="beer_delete"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]