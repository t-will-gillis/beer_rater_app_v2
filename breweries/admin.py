from django.contrib import admin

from .models import Brewery


class BreweryAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "state", "country", "url", "num_beers", "avg_score")


admin.site.register(Brewery, BreweryAdmin)