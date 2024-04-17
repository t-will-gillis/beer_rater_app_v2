from django.db import models
from django.urls import reverse
import json
import uuid

def get_styles():
    with open("./staticfiles/beaut_soup/styles.json") as file:
        styles = json.load(file)
    tuple(styles)
    return styles


class Beer(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=64)
    style = models.CharField(max_length=64, choices=get_styles(), default="21c")
    abv = models.DecimalField(max_digits=3, decimal_places=1)
    avg_score = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    num_reviews = models.IntegerField(default=0)
    beer_notes = models.TextField(blank=True)
    brewery = models.ForeignKey(
        "breweries.Brewery",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="beers",
    )
    label = models.ImageField(upload_to="labels/", blank=True)

    class Meta:
        permissions = [
            ("special_status", "Can read all beers"),
        ]
    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("beer_detail", args=[str(self.id)])
    

