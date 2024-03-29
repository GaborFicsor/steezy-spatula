# Generated by Django 3.2.18 on 2023-03-17 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20230317_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='allergens',
        ),
        migrations.AddField(
            model_name='recipe',
            name='allergens',
            field=models.ManyToManyField(choices=[(0, 'None'), (1, 'Vegan'), (2, 'Vegetarian'), (3, 'Gluten-free'), (4, 'Contains nuts'), (5, 'Dairy-free')], default=0, to='recipes.Allergens'),
        ),
    ]
