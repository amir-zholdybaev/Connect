from django.db import models
from general_app.models import User
from django.utils.translation import gettext_lazy as _


class Channel(models.Model):
    name = models.CharField(_('name'), max_length=150)
    description = models.TextField()
    owner = models.ForeignKey(
        _('owner'),
        to=User,
        on_delete=models.CASCADE,
        related_name="channels",
        default=1
    )
    admins = models.ManyToManyField(
        _('administrators'),
        to=User,
        related_name='admin_channels',
        null=True
    )
    subscribers = models.ManyToManyField(
        _('subscribers'),
        to=User,
        related_name='subscriber_channels',
        null=True
    )


class Post(models.Model):
    channel = models.ForeignKey(
        _('channel'),
        to=Channel,
        on_delete=models.CASCADE,
        related_name="posts",
        default=1
    )
    author = models.ForeignKey(
        _('author'),
        to=User, 
        on_delete=models.CASCADE,
        related_name="posts",
        default=1
    )
    title = models.CharField(_('title'), max_length=150, blank=True, null=True)
    body = models.TextField(_('body'), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    created_at = models.DateTimeField(auto_now_add=True)
