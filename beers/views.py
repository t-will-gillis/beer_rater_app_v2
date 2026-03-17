from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import BeerForm
from .models import Beer


def _approved_beers(user):
    qs = Beer.objects.select_related("brewery").filter(is_approved=True)
    if user.is_authenticated:
        qs = (qs | Beer.objects.select_related("brewery").filter(submitted_by=user)).distinct()
    return qs


class BeerListView(
        # LoginRequiredMixin,
        ListView):
    model = Beer
    context_object_name = "beer_list"
    template_name = "beers/beer_list.html"
    login_url = "account_login"

    def get_queryset(self):
        return _approved_beers(self.request.user)


class BeerDetailView(
        # LoginRequiredMixin,
        # PermissionRequiredMixin,
        DetailView):
    model = Beer
    context_object_name = "beer"
    template_name = "beers/beer_detail.html"
    # login_url = "account_login"
    # permission_required = "beers.special_status"

    def get_queryset(self):
        return _approved_beers(self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = self.object.reviews.select_related("author").filter(is_approved=True)
        if self.request.user.is_authenticated:
            reviews = (reviews | self.object.reviews.select_related("author").filter(author=self.request.user)).distinct()
        context["reviews"] = reviews
        return context


class SearchResultsListView(ListView):
    model = Beer
    context_object_name = "beer_list"
    template_name = "beers/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return _approved_beers(self.request.user).filter(
            Q(name__icontains=query) | Q(style__icontains=query)
        )


class BeerCreateView(LoginRequiredMixin, CreateView):
    model = Beer
    form_class = BeerForm
    template_name = "beers/beer_form.html"
    login_url = "account_login"

    def form_valid(self, form):
        form.instance.submitted_by = self.request.user
        return super().form_valid(form)


class BeerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Beer
    form_class = BeerForm
    template_name = "beers/beer_form.html"
    login_url = "account_login"

    def test_func(self):
        beer = self.get_object()
        return self.request.user == beer.submitted_by

    def form_valid(self, form):
        form.instance.is_approved = False
        return super().form_valid(form)


class BeerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Beer
    template_name = "beers/beer_confirm_delete.html"
    success_url = reverse_lazy("beer_list")
    login_url = "account_login"

    def test_func(self):
        beer = self.get_object()
        return self.request.user == beer.submitted_by
