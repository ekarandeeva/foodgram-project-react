# Generated by Django 3.2 on 2023-06-15 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20230615_1515'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='tag',
            name='unique_color_font_size',
        ),
    ]
