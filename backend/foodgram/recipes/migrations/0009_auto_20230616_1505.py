# Generated by Django 3.2 on 2023-06-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_remove_tag_unique_color_font_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='font_size',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название'),
        ),
    ]
