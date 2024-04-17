from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.views.generic import ListView, DetailView

from .models import Beer


class BeerListView(
        # LoginRequiredMixin, 
        ListView):
    model = Beer
    context_object_name = "beer_list"
    template_name = "beers/beer_list.html"
    login_url = "account_login"


class BeerDetailView(
        # LoginRequiredMixin,
        # PermissionRequiredMixin,
        DetailView):
    model = Beer
    context_object_name = "beer"
    template_name = "beers/beer_detail.html"
    # login_url = "account_login"
    # permission_required = "beers.special_status"
