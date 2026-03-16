from django import forms

from .models import Brewery


class BreweryForm(forms.ModelForm):
    class Meta:
        model = Brewery
        fields = (
            "name",
            "city",
            "state",
            "country",
            "url",
        )
