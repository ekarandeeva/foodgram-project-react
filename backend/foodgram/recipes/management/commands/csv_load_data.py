import json

from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Add data to bd'

    def handle(self, *args, **options):

        with open('recipes/data/ingredients.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

            for ingredients in data:
                name = ingredients['name']
                measurement_unit = ingredients['measurement_unit']
                Ingredient.objects.create(
                    name=name,
                    measurement_unit=measurement_unit
                )
        print('finished')
