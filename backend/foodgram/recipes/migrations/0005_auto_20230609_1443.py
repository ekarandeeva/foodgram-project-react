# Generated by Django 3.2 on 2023-06-09 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipeingredient_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='preparation_time',
            new_name='cooking_time',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='description',
            new_name='text',
        ),
    ]
