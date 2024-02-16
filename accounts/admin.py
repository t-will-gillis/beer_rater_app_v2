from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        # "city",
        # "state",
        # "country",
        "email",
        "is_superuser",
    ]
    # fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("city","state","country",)}),)
    # add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("city","state","country",)}),)


admin.site.register(CustomUser, CustomUserAdmin)