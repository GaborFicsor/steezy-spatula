# Generated by Django 3.2.18 on 2023-03-16 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20230316_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergens',
            name='allergen',
            field=models.CharField(choices=[(0, 'None'), (1, 'Vegan'), (2, 'Vegetarian'), (3, 'Gluten-free'), (4, 'Contains nuts'), (5, 'Dairy-free')], max_length=50),
        ),
        migrations.AlterField(
            model_name='mainingredient',
            name='main_ingredient_name',
            field=models.CharField(choices=[(0, 'Chicken'), (1, 'Noodles'), (2, 'Fish'), (3, 'Beef'), (4, 'Fruit'), (5, 'Pork'), (6, 'Rice'), (7, 'Seafood'), (8, 'Potato'), (9, 'Bread'), (10, 'Vegetables'), (11, 'Eggs'), (12, 'Oats')], max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='allergens',
            field=models.ManyToManyField(choices=[(0, 'None'), (1, 'Vegan'), (2, 'Vegetarian'), (3, 'Gluten-free'), (4, 'Contains nuts'), (5, 'Dairy-free')], to='recipes.Allergens'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='main_ingredient',
            field=models.ManyToManyField(choices=[(0, 'Chicken'), (1, 'Noodles'), (2, 'Fish'), (3, 'Beef'), (4, 'Fruit'), (5, 'Pork'), (6, 'Rice'), (7, 'Seafood'), (8, 'Potato'), (9, 'Bread'), (10, 'Vegetables'), (11, 'Eggs'), (12, 'Oats')], to='recipes.MainIngredient'),
        ),
    ]