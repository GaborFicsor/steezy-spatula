# Generated by Django 3.2.18 on 2023-03-17 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20230317_1138'),
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
            field=models.ManyToManyField(choices=[('None', 'None'), ('Vegan', 'Vegan'), ('Vegetarian', 'Vegetarian'), ('Gluten-free', 'Gluten-free'), ('Contains nuts', 'Contains nuts'), ('Dairy-free', 'Dairy-free')], default=0, to='recipes.Allergens'),
        ),
    ]
