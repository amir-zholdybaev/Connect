from django.db import models
from users_app.models import User
from django.utils.translation import gettext_lazy as _


class Channel(models.Model):
    name = models.CharField(_('name'), max_length=150)
    description = models.TextField()
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="channels",
        verbose_name=_('owner'),
        default=1
    )
    admins = models.ManyToManyField(
        to=User,
        related_name='admin_channels',
        verbose_name=_('administrators'),
        null=True
    )
    subscribers = models.ManyToManyField(
        to=User,
        related_name='subscriber_channels',
        verbose_name=_('subscribers'),
        null=True
    )


class Post(models.Model):
    channel = models.ForeignKey(
        to=Channel,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name=_('channel'),
        default=1
    )
    author = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name=_('author'),
        default=1,
    )
    title = models.CharField(_('title'), max_length=150, blank=True, null=True)
    body = models.TextField(_('body'), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Reaction(models.Model):
    class Values(models.TextChoices):
        SMILE = "smile", "Улыбка"
        THUMB_UP = "thumb_up", "Большой палец вверх"
        LAUGH = "laugh", "Смех"
        SAD = "sad", "Грусть"
        HEART = "heart", "Сердце"

    value = models.CharField(max_length=8, choices=Values.choices, null=True)
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="reactions",
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="reactions",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                "author",
                "post",
                name="author_post_unique",
            ),
        ]


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
