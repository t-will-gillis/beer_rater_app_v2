from django.contrib import admin
from .models import Beer
from reviews.models import Review


class ReviewInline(admin.TabularInline):
    model = Review


def approve_beers(modeladmin, request, queryset):
    queryset.update(is_approved=True)
approve_beers.short_description = "Approve selected beers"


class BeerAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    actions = [approve_beers]
    list_display = ("name", "style", "abv", "avg_score", "num_reviews", "is_approved", "submitted_by")
    list_filter = ("is_approved",)


admin.site.register(Beer, BeerAdmin)
