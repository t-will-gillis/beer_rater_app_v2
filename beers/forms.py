from django import forms
from django.core.exceptions import ValidationError

from .models import Beer, get_styles


def validate_image_size(file):
    if file.size > 5 * 1024 * 1024:
        raise ValidationError("Image file too large (max 5 MB).")


class BeerForm(forms.ModelForm):
    label = forms.ImageField(required=False, validators=[validate_image_size])

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
