from django.urls import path

from .views import ReviewCreateView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path("beer/<uuid:pk>/add/", ReviewCreateView.as_view(), name="review_create"),
    path("<int:pk>/edit/", ReviewUpdateView.as_view(), name="review_update"),
    path("<int:pk>/delete/", ReviewDeleteView.as_view(), name="review_delete"),
]
