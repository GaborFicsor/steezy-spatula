# Generated by Django 3.2.18 on 2023-03-15 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20230315_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allergens',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='mainingredient',
            name='recipe',
        ),
        migrations.AddField(
            model_name='recipe',
            name='allergens',
            field=models.ManyToManyField(to='recipes.Allergens'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='main_ingredient',
            field=models.ManyToManyField(to='recipes.MainIngredient'),
        ),
    ]
