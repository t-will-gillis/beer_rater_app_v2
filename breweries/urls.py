from django.urls import path

from .views import BreweryListView, BreweryDetailView

urlpatterns = [
    path("", BreweryListView.as_view(), name="brewery_list"),
    path("<uuid:pk>", BreweryDetailView.as_view(), name="brewery_detail"),
]