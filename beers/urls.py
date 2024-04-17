from django.urls import path

from .views import BeerListView, BeerDetailView, SearchResultsListView


urlpatterns = [
    path("", BeerListView.as_view(), name="beer_list"),
    path("<uuid:pk>/", BeerDetailView.as_view(), name="beer_detail"),
    path("search/", SearchResultsListView.as_view(),
         name="search_results"),
]