# Generated by Django 3.2.18 on 2023-03-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20230317_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='main_ingredient',
            field=models.IntegerField(choices=[(0, 'Chicken'), (1, 'Noodles'), (2, 'Fish'), (3, 'Beef'), (4, 'Fruit'), (5, 'Pork'), (6, 'Rice'), (7, 'Seafood'), (8, 'Potato'), (9, 'Bread'), (10, 'Vegetables'), (11, 'Eggs'), (12, 'Oats')], default=0),
        ),
        migrations.DeleteModel(
            name='MainIngredient',
        ),
    ]