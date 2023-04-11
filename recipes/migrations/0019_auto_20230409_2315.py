# Generated by Django 3.2.18 on 2023-04-09 23:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0018_auto_20230409_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='saved',
        ),
        migrations.AddField(
            model_name='recipe',
            name='saves',
            field=models.ManyToManyField(blank=True, related_name='recipe_saves', to=settings.AUTH_USER_MODEL),
        ),
    ]
