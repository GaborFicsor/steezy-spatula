# Generated by Django 3.2.18 on 2023-04-17 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0024_auto_20230417_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='calories_per_serving',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='serving_size',
            field=models.PositiveIntegerField(),
        ),
    ]