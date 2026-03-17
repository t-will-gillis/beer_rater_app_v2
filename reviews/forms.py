from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from beers.forms import validate_image_size
from .models import Review


class ReviewForm(forms.ModelForm):
    image = forms.ImageField(required=False, validators=[validate_image_size])
    overall = forms.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )

    class Meta:
        model = Review
        fields = (
            "overall",
            "review",
            "image",
            # "location",
            # "container",
            # "size",
        )
        widgets = {
            "image": forms.ClearableFileInput(attrs={
                "accept": "image/*",
                "capture": "environment",
            }),
        }
