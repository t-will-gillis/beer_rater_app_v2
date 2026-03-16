from django.contrib import admin
from .models import Review


def approve_reviews(modeladmin, request, queryset):
    queryset.update(is_approved=True)
approve_reviews.short_description = "Approve selected reviews"


class ReviewAdmin(admin.ModelAdmin):
    actions = [approve_reviews]
    list_display = ("beer", "author", "overall", "is_approved")
    list_filter = ("is_approved",)


admin.site.register(Review, ReviewAdmin)
