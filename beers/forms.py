from django import forms

from .models import Beer, get_styles


class BeerForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = (
            "name",
            "style",
            "abv",
            "brewery",
            "beer_notes",
            "label",
        )
