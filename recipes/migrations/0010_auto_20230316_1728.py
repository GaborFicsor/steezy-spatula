# Generated by Django 3.2.18 on 2023-03-16 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_auto_20230316_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergens',
            name='allergen',
            field=models.CharField(choices=[('None', 'None'), ('Vegan', 'Vegan'), ('Vegetarian', 'Vegetarian'), ('Gluten-free', 'Gluten-free'), ('Contains nuts', 'Contains nuts'), ('Dairy-free', 'Dairy-free')], max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='allergens',
            field=models.ManyToManyField(choices=[('None', 'None'), ('Vegan', 'Vegan'), ('Vegetarian', 'Vegetarian'), ('Gluten-free', 'Gluten-free'), ('Contains nuts', 'Contains nuts'), ('Dairy-free', 'Dairy-free')], default='None', to='recipes.Allergens'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.DurationField(choices=[(datetime.timedelta(seconds=300), '5 mins'), (datetime.timedelta(seconds=600), '10 mins'), (datetime.timedelta(seconds=900), '15 mins'), (datetime.timedelta(seconds=1200), '20 mins'), (datetime.timedelta(seconds=1500), '25 mins'), (datetime.timedelta(seconds=1800), '30 mins'), (datetime.timedelta(seconds=2100), '35 mins'), (datetime.timedelta(seconds=2400), '40 mins'), (datetime.timedelta(seconds=2700), '45 mins'), (datetime.timedelta(seconds=3000), '50 mins'), (datetime.timedelta(seconds=3300), '55mins'), (datetime.timedelta(seconds=3600), '1 hour')], default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep_time',
            field=models.DurationField(choices=[(datetime.timedelta(seconds=300), '5 mins'), (datetime.timedelta(seconds=600), '10 mins'), (datetime.timedelta(seconds=900), '15 mins'), (datetime.timedelta(seconds=1200), '20 mins'), (datetime.timedelta(seconds=1500), '25 mins'), (datetime.timedelta(seconds=1800), '30 mins'), (datetime.timedelta(seconds=2100), '35 mins'), (datetime.timedelta(seconds=2400), '40 mins'), (datetime.timedelta(seconds=2700), '45 mins'), (datetime.timedelta(seconds=3000), '50 mins'), (datetime.timedelta(seconds=3300), '55mins'), (datetime.timedelta(seconds=3600), '1 hour')], default=datetime.timedelta(0)),
        ),
    ]
