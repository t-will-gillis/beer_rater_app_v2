from django.contrib import admin

from .models import Brewery


def approve_breweries(modeladmin, request, queryset):
    queryset.update(is_approved=True)
approve_breweries.short_description = "Approve selected breweries"


class BreweryAdmin(admin.ModelAdmin):
    actions = [approve_breweries]
    list_display = ("name", "city", "state", "country", "num_beers", "avg_score", "is_approved", "submitted_by")
    list_filter = ("is_approved",)


admin.site.register(Brewery, BreweryAdmin)