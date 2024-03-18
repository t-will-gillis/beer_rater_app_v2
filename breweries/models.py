from django.db import models
from django.urls import reverse
import uuid

class Brewery(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64, blank=True)
    state = models.CharField(max_length=2, blank=True)
    country = models.CharField(max_length=32, blank=True)
    url = models.URLField(blank=True)
    num_beers = models.IntegerField(default=0)
    avg_score = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("brewery_detail", args=[str(self.id)])