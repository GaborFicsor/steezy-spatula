# Generated by Django 3.2.18 on 2023-03-16 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20230315_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='allergens',
            field=models.ManyToManyField(choices=[('Vegan', 'Vegan'), ('Vegetarian', 'Vegetarian'), ('Gluten-free', 'Gluten-free'), ('Contains nuts', 'Contains nuts'), ('Dairy-free', 'Dairy-free')], to='recipes.Allergens'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='main_ingredient',
            field=models.ManyToManyField(choices=[('Chicken', 'Chicken'), ('Noodles', 'Noodles'), ('Fish', 'Fish'), ('Beef', 'Beef'), ('Fruit', 'Fruit'), ('Pork', 'Pork'), ('Rice', 'Rice'), ('Seafood', 'Seafood'), ('Potato', 'Potato'), ('Bread', 'Bread'), ('Vegetables', 'Vegetables'), ('Eggs', 'Eggs')], to='recipes.MainIngredient'),
        ),
    ]
