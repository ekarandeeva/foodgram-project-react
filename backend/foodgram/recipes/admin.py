from django.contrib import admin

from .models import (Favorite, Ingredient, Recipe, RecipeIngredient,
                     ShoppingCart, Tag)


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'color',
        'slug'
    )
    search_fields = (
        'name',
        'color',
        'slug'
    )
    list_filter = (
        'name',
        'color',
        'slug'
    )
    empty_value_display = '-пусто-'


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'measurement_unit'
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
    )
    empty_value_display = '-пусто-'


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'author',
        'favorites_amount'
    )
    search_fields = (
        'name',
        'author'
    )
    list_filter = (
        'name',
        'author',
        'tags'
    )
    empty_value_display = '-пусто-'
    inlines = [
        RecipeIngredientInline,
    ]

    def favorites_amount(self, obj):
        return obj.favorites.count()


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'recipe',
        'ingredient',
        'amount'
    )
    empty_value_display = '-пусто-'


class AbstractUserItemAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'recipe'
    )
    search_fields = (
        'user',
        'recipe'
    )
    empty_value_display = '-пусто-'


class FavoriteAdmin(AbstractUserItemAdmin):
    pass


class ShoppingCartAdmin(AbstractUserItemAdmin):
    pass


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
