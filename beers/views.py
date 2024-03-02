from django.views.generic import ListView, DetailView

from .models import Beer


class BeerListView(ListView):
    model = Beer
    context_object_name = "beer_list"
    template_name = "beers/beer_list.html"


class BeerDetailView(DetailView):
    model = Beer
    context_object_name = "beer"
    template_name = "beers/beer_detail.html"
