# Generated by Django 3.2.18 on 2023-04-17 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0020_alter_recipe_difficulty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='likes',
        ),
    ]
