from django.db.models import Q
from django_filters.rest_framework import FilterSet, filters
from recipes.models import Ingredient, Recipe, Tag


class RecipeFilter(FilterSet):
    tags = filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        field_name='tags__slug',
        to_field_name='slug',
    )
    is_favorited = filters.BooleanFilter(
        method='get_is_favorited'
    )
    is_in_shopping_cart = filters.BooleanFilter(
        method='get_is_in_shopping_cart'
    )

    class Meta:
        model = Recipe
        fields = ('author', 'tags', 'is_favorited', 'is_in_shopping_cart')

    def get_is_favorited(self, queryset, name, value):
        if self.request.user.is_authenticated and value:
            return queryset.filter(favorites__user=self.request.user)
        return queryset

    def filter_queryset(self, queryset):
        filters = Q()
        if 'is_in_shopping_cart' in self.request.GET and \
                self.request.user.is_authenticated:
            is_in_shopping_cart = self.request.GET.get('is_in_shopping_cart')
            if is_in_shopping_cart.lower() == 'true':
                filters |= Q(shoppingcarts__user=self.request.user)
        queryset = queryset.filter(filters)
        return super().filter_queryset(queryset)


class IngredientFilter(FilterSet):
    name = filters.CharFilter(
        field_name='name',
        lookup_expr='istartswith'
    )

    class Meta:
        model = Ingredient
        fields = ('name', 'measurement_unit')
