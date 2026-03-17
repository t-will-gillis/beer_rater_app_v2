from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import BreweryForm
from .models import Brewery


def _approved_breweries(user):
    qs = Brewery.objects.filter(is_approved=True)
    if user.is_authenticated:
        qs = (qs | Brewery.objects.filter(submitted_by=user)).distinct()
    return qs


class BreweryListView(ListView):
    model = Brewery
    context_object_name = "brewery_list"
    template_name = "breweries/brewery_list.html"

    def get_queryset(self):
        return _approved_breweries(self.request.user)


class BreweryDetailView(DetailView):
    model = Brewery
    context_object_name = "brewery"
    template_name = "breweries/brewery_detail.html"

    def get_queryset(self):
        return _approved_breweries(self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from beers.models import Beer
        beers = self.object.beers.filter(is_approved=True)
        if self.request.user.is_authenticated:
            beers = (beers | self.object.beers.filter(submitted_by=self.request.user)).distinct()
        context["approved_beers"] = beers
        return context


class BreweryCreateView(LoginRequiredMixin, CreateView):
    model = Brewery
    form_class = BreweryForm
    template_name = "breweries/brewery_form.html"
    login_url = "account_login"

    def form_valid(self, form):
        form.instance.submitted_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={self.request.get_host()}):
            return next_url
        return super().get_success_url()


class BreweryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Brewery
    form_class = BreweryForm
    template_name = "breweries/brewery_form.html"
    login_url = "account_login"

    def test_func(self):
        brewery = self.get_object()
        return self.request.user == brewery.submitted_by

    def form_valid(self, form):
        form.instance.is_approved = False
        return super().form_valid(form)


class BreweryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Brewery
    template_name = "breweries/brewery_confirm_delete.html"
    success_url = reverse_lazy("brewery_list")
    login_url = "account_login"

    def test_func(self):
        brewery = self.get_object()
        return self.request.user == brewery.submitted_by
