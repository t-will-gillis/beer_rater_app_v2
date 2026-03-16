from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from beers.models import Beer
from .forms import ReviewForm
from .models import Review


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_form.html"
    login_url = "account_login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.beer = get_object_or_404(Beer, pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["beer"] = get_object_or_404(Beer, pk=self.kwargs["pk"])
        return context

    def get_success_url(self):
        return reverse("beer_detail", args=[str(self.kwargs["pk"])])


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_form.html"
    login_url = "account_login"

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author

    def form_valid(self, form):
        form.instance.is_approved = False
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("beer_detail", args=[str(self.object.beer.pk)])


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = "reviews/review_confirm_delete.html"
    login_url = "account_login"

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author

    def get_success_url(self):
        return reverse("beer_detail", args=[str(self.object.beer.pk)])
