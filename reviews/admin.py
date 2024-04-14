from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("overall", "review", "author")

admin.site.register(Review, ReviewAdmin)
