from django_filters import rest_framework
from django_filters import rest_framework as filters
from recipes.models import Ingredient, Recipe, Tag


class RecipeAnonymousFilters(rest_framework.FilterSet):
    """Возможность фильтровать рецепты только по тэгу
    для анонимных пользователей."""

    tags = rest_framework.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        queryset=Tag.objects.all(),
        to_field_name='slug',
    )

    class Meta:
        model = Recipe
        fields = ('tags',)


class RecipeFilter(filters.FilterSet):
    # tags = filters.ModelMultipleChoiceFilter(
    #     queryset=Tag.objects.all(),
    #     field_name='tags__slug',
    #     to_field_name='slug',
    # )
    is_favorited = filters.BooleanFilter(
        field_name='favorites',
        method='get_is_in_shopping_cart'
    )
    is_in_shopping_cart = filters.BooleanFilter(
        field_name='shoppingcarts',
        method='get_is_in_shopping_cart'
    )
    author = rest_framework.NumberFilter(field_name='author__id')

    class Meta:
        model = RecipeAnonymousFilters.Meta.model
        fields = RecipeAnonymousFilters.Meta.fields + ('author',)

    # class Meta:
    #     model = Recipe
    #     fields = ('author', 'tags', 'is_favorited', 'is_in_shopping_cart')

    # def get_is_favorited(self, queryset, name, value):
    #     if self.request.user.is_authenticated and value:
    #         return queryset.filter(favorites__user=self.request.user)
    #     return queryset

    # def get_is_in_shopping_cart(self, queryset, name, value):
    #     if self.request.user.is_authenticated and value:
    #         return queryset.filter(carts__user=self.request.user)
    #     return queryset

    def get_is_in_shopping_cart(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(
            id__in=self.request.user.favorites.values_list('recipe')
            if name == 'favorites'
            else self.request.user.shoppings.values_list('recipe')
        )


class IngredientFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name='name',
        lookup_expr='istartswith'
    )

    class Meta:
        model = Ingredient
        fields = ('name', 'measurement_unit')
