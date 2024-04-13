from django.test import TestCase
from django.urls import reverse

from .models import Brewery 


class BreweryTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.brewery = Brewery.objects.create(
            name="New Belgium",
            city="Fort Collins",
            state="CO",
            url="www.newbelgium.com",
        )

    def test_brewery_listing(self):
        self.assertEqual(f"{self.brewery.name}", "New Belgium")
        self.assertEqual(f"{self.brewery.city}", "Fort Collins")
        self.assertEqual(f"{self.brewery.state}", "CO")
        self.assertEqual(f"{self.brewery.url}", "www.newbelgium.com")

    def test_brewery_list_view(self):
        response = self.client.get(reverse("brewery_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New Belgium")
        self.assertTemplateUsed(response, "breweries/brewery_list.html")

    def test_brewery_detail_view(self):
        response = self.client.get(self.brewery.get_absolute_url())
        no_response = self.client.get("/breweries/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Fort Collins")
        self.assertTemplateUsed(response, "breweries/brewery_detail.html")