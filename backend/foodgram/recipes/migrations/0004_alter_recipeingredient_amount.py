# Generated by Django 3.2 on 2023-06-09 13:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20230604_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='amount',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, 'Количество ингредиентов не может быть меньше одного'), django.core.validators.MaxValueValidator(32767, 'Количество ингредиентов превышает допустимое значение')], verbose_name='Количество'),
        ),
    ]
