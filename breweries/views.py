from django.views.generic import ListView, DetailView

from .models import Brewery


class BreweryListView(ListView):
    model = Brewery
    context_object_name = "brewery_list"
    template_name = "breweries/brewery_list.html"


class BreweryDetailView(DetailView):
    model = Brewery
    context_object_name = "brewery"
    template_name = "breweries/brewery_detail.html"
