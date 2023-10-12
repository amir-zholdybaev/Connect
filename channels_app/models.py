from django.db import models
from django.utils.translation import gettext_lazy as _

from users_app.models import User


class Channel(models.Model):
    name = models.CharField(_('name'), max_length=150)
    description = models.TextField(_('description'), blank=True)
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="channels",
        verbose_name=_('owner')
    )
    admins = models.ManyToManyField(
        to=User,
        related_name='admin_channels',
        verbose_name=_('administrators'),
        blank=True
    )
    subscribers = models.ManyToManyField(
        to=User,
        related_name='subscriber_channels',
        verbose_name=_('subscribers'),
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(_('title'), max_length=150, blank=True)
    body = models.TextField(_('body'), blank=True)
    image = models.ImageField(blank=True, upload_to='images')
    channel = models.ForeignKey(
        to=Channel,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name=_('channel')
    )
    author = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name=_('author')
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Reaction(models.Model):
    class Values(models.TextChoices):
        THUMB_UP = "thumb up", _("thumb up")
        THUMB_DOWN = "thumb down", _("thumb down")

    value = models.CharField(max_length=10, choices=Values.choices)
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="reactions",
        verbose_name=_('author')
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="reactions",
        verbose_name=_('post')
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                "author",
                "post",
                name="author_post_unique",
            ),
        ]
    
    def __str__(self) -> str:
        return self.value


class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_('author')
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_('post')
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        if len(self.body) > 25:
            return f'{self.body[:25]}...'
        
        return self.body
