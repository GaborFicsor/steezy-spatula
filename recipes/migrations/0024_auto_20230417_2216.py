# Generated by Django 3.2.18 on 2023-04-17 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0023_remove_recipe_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='eggs',
        ),
        migrations.AddField(
            model_name='recipe',
            name='vegan',
            field=models.BooleanField(default=False),
        ),
    ]
