# Generated by Django 3.2.18 on 2023-04-17 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0027_auto_20230417_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='status',
        ),
    ]