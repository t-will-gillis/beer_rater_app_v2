from django.contrib import admin

from .models import Beer


class BeerAdmin(admin.ModelAdmin):
    list_display = ("name", "style", "abv", "avg_score", "num_reviews",)


admin.site.register(Beer, BeerAdmin)
