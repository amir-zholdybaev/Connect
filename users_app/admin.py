from django.contrib import admin

from .models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "username",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
        "date_joined",
    )