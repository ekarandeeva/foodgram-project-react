# Generated by Django 3.2 on 2023-06-16 18:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_alter_recipeingredient_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='amount',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1, 'Количество ингредиентов не может быть меньше одного'), django.core.validators.MaxValueValidator(1e+21, 'Количество ингредиентов превышает допустимое значение')], verbose_name='Количество'),
        ),
    ]