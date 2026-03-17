from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from PIL import Image


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
    image = models.ImageField(upload_to="reviews/", blank=True)
    is_approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            img.thumbnail((800, 800))
            img.save(self.image.path)

    def __str__(self):
        return f"{self.review}"
