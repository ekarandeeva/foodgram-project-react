from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters
from recipes.models import Ingredient, Recipe

User = get_user_model()


# class RecipeAnonymousFilters(rest_framework.FilterSet):
#     """Возможность фильтровать рецепты только по тэгу
#     для анонимных пользователей."""

#     tags = rest_framework.ModelMultipleChoiceFilter(
#         field_name='tags__slug',
#         queryset=Tag.objects.all(),
#         to_field_name='slug',
#     )

#     class Meta:
#         model = Recipe
#         fields = ('tags',)


# class RecipeFilter(filters.FilterSet):
#     is_favorited = filters.BooleanFilter(
#         field_name='favorites',
#         method='get_is_in_shopping_cart'
#     )
#     is_in_shopping_cart = filters.BooleanFilter(
#         field_name='shoppings',
#         method='get_is_in_shopping_cart'
#     )
#     author = rest_framework.NumberFilter(field_name='author__id')

#     class Meta:
#         model = RecipeAnonymousFilters.Meta.model
#         fields = RecipeAnonymousFilters.Meta.fields + ('author',)

#     def get_is_in_shopping_cart(self, queryset, name, value):
#         if not value:
#             return queryset
#         return queryset.filter(
#             id__in=self.request.user.favorites.values_list('recipe')
#             if name == 'favorites'
#             else self.request.user.shoppings.values_list('recipe')
#         )


class RecipeFilter(filters.FilterSet):
    is_favorited = filters.BooleanFilter(method='filter_is_favorited')
    is_in_shopping_cart = filters.BooleanFilter(
        method='filter_is_in_shopping_cart'
    )
    tags = filters.AllValuesMultipleFilter(field_name='tags__slug')
    author = filters.ModelChoiceFilter(
        queryset=User.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ('tags', 'author', 'is_favorited', 'is_in_shopping_cart')

    def filter_is_favorited(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            return queryset.filter(favorites__user=self.request.user)
        return queryset

    def filter_is_in_shopping_cart(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            return queryset.filter(shopping_cart__user=self.request.user)
        return queryset


class IngredientFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name='name',
        lookup_expr='istartswith'
    )

    class Meta:
        model = Ingredient
        fields = ('name', 'measurement_unit')
