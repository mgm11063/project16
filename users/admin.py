from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class UserAdmin(UserAdmin):
    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "커스텀 필드",
            {"fields": ("bio",)},
        ),
    )
