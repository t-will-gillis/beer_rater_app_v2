from django.urls import path

from .views import (
    BreweryListView,
    BreweryDetailView,
    BreweryCreateView,
    BreweryUpdateView,
    BreweryDeleteView,
)

urlpatterns = [
    path("", BreweryListView.as_view(), name="brewery_list"),
    path("<uuid:pk>/", BreweryDetailView.as_view(), name="brewery_detail"),
    path("add/", BreweryCreateView.as_view(), name="brewery_create"),
    path("<uuid:pk>/edit/", BreweryUpdateView.as_view(), name="brewery_update"),
    path("<uuid:pk>/delete/", BreweryDeleteView.as_view(), name="brewery_delete"),
]