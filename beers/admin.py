from django.contrib import admin
from .models import Beer
from reviews.models import Review


class ReviewInline(admin.TabularInline):
    model = Review

class BeerAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("name", "style", "abv", "avg_score", "num_reviews",)


admin.site.register(Beer, BeerAdmin)
