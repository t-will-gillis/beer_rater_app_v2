from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Review(models.Model):
    beer = models.ForeignKey(
        "beers.Beer",
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review = models.CharField(max_length=512)
    overall = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    # appear = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    # smell = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    # taste = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    # feel = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.review}"
