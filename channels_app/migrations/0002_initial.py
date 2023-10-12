# Generated by Django 4.2.5 on 2023-10-12 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('channels_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reaction',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='reaction',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='channels_app.post', verbose_name='post'),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='post',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='channels_app.channel', verbose_name='channel'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='channels_app.post', verbose_name='post'),
        ),
        migrations.AddField(
            model_name='channel',
            name='admins',
            field=models.ManyToManyField(blank=True, related_name='admin_channels', to=settings.AUTH_USER_MODEL, verbose_name='administrators'),
        ),
        migrations.AddField(
            model_name='channel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channels', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='channel',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='subscriber_channels', to=settings.AUTH_USER_MODEL, verbose_name='subscribers'),
        ),
        migrations.AddConstraint(
            model_name='reaction',
            constraint=models.UniqueConstraint(models.F('author'), models.F('post'), name='author_post_unique'),
        ),
    ]