from django.test import TestCase
from django.urls import reverse

from .models import Beer


class BeerTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.beer = Beer.objects.create(
        name="Fatter Tire",
        style="1b",
        abv="4.5",
        )

    def test_beer_listing(self):
        self.assertEqual(f"{self.beer.name}", "Fatter Tire")
        self.assertEqual(f"{self.beer.style}", "1b")
        self.assertEqual(f"{self.beer.abv}", "4.5")

    def test_beer_list_view(self):
        response = self.client.get(reverse("beer_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fatter Tire")
        self.assertTemplateUsed(response, "beers/beer_list.html")

    def test_beer_detail_view(self):
        response = self.client.get(self.beer.get_absolute_url())
        no_response = self.client.get("/beers/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Fatter Tire")
        self.assertTemplateUsed(response, "beers/beer_detail.html")

