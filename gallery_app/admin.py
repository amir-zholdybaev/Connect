from django.contrib import admin

from .models import Image

@admin.register(Image)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "image"
    )