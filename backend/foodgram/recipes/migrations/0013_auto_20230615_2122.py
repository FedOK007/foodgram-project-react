# Generated by Django 3.2 on 2023-06-15 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_auto_20230615_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='favorites',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='shoppingcarts',
        ),
    ]