from django.contrib import admin

from .models import *


@admin.register(Channel)
class ChannelModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "owner",
    )


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "body",
        "image",
        "channel",
        "author",
        "created_at"
    )


@admin.register(Reaction)
class ReactionModelAdmin(admin.ModelAdmin):
    list_display = (
        "value",
        "author",
        "post",
    )


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = (
        "body",
        "author",
        "post",
        "created_at"
    )