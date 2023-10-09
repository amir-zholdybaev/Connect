# Generated by Django 4.2.5 on 2023-10-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('currency', models.CharField(choices=[('E', 'Euro'), ('D', 'Dollar'), ('R', 'Rubles')], default='R', max_length=1)),
            ],
        ),
    ]
