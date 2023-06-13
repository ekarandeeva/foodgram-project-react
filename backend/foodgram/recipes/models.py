from colorfield.fields import ColorField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User


class Tag(models.Model):
    name = models.CharField(
        'Название',
        max_length=200,
        unique=True
    )
    color = ColorField(
        'Цвет'
    )
    slug = models.SlugField(
        'Слаг',
        max_length=200,
        unique=True
    )
    font_size = models.IntegerField(
        'Размер шрифта',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        constraints = [
            models.UniqueConstraint(
                fields=['color', 'font_size'],
                name='unique_color_font_size'
            )
        ]

    def __str__(self):
        return self.name[:50]


class Ingredient(models.Model):
    name = models.CharField(
        'Название',
        max_length=200,
        unique=True
    )
    measurement_unit = models.CharField(
        'Единица измерения',
        max_length=200
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name[:50]


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор',
    )
    name = models.CharField(
        'Название',
        max_length=200)
    image = models.ImageField(
        'Картинка',
        upload_to='recipes/'
    )
    text = models.TextField(
        'Описание',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name='Ингридиенты',
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
    )
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления',
        validators=[
            MinValueValidator(
                1, 'Время приготовления не должно быть меньше единицы'
            ),
            MaxValueValidator(
                32767, 'Время приготовления превышает допустимое значение'
            )
        ]
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name[:50]


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipeingredients',
        verbose_name='Рецепт',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipeingredients',
        verbose_name='Ингредиент',
    )
    amount = models.BigIntegerField(
        'Количество',
        validators=[
            MinValueValidator(
                1, 'Количество ингредиентов не может быть меньше одного'
            ),
            MaxValueValidator(
                32767, 'Количество ингредиентов превышает допустимое значение'
            )
        ]
    )

    class Meta:
        verbose_name = 'Ингредиент в рецепте'
        verbose_name_plural = 'Ингредиенты в рецепте'
        ordering = ('amount',)
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_ingredient_for_recipe',
            )
        ]

    def __str__(self):
        return (f'{self.recipe.name}: '
                f'{self.ingredient.name} - '
                f'{self.amount} '
                f'{self.ingredient.measurement_unit}')


class AbstractUserItem(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='%(class)ss',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='%(class)ss',
        verbose_name='Рецепт'
    )

    class Meta:
        abstract = True
        ordering = ('-id',)


class Favorite(AbstractUserItem):
    class Meta(AbstractUserItem.Meta):
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_user_favorite_recipe'
            )
        ]

    def __str__(self):
        return f'{self.user.username} добавил в Избранное {self.recipe.name}.'


class ShoppingCart(AbstractUserItem):
    class Meta(AbstractUserItem.Meta):
        verbose_name = 'Cписок покупок'
        verbose_name_plural = 'Cписки покупок'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_user_shoppingcart_recipe'
            )
        ]

    def __str__(self):
        return (f'{self.user.username} добавил'
                f'{self.recipe.name} в список покупок.')


# class CartItem(models.Model):
#     shopping_cart = models.ForeignKey(
#         ShoppingCart,
#         on_delete=models.CASCADE,
#         verbose_name='Список покупок'
#     )
#     recipe = models.ForeignKey(
#         Recipe,
#         on_delete=models.CASCADE,
#         verbose_name='Рецепт'
#     )
#     quantity = models.PositiveIntegerField(verbose_name='Количество')

#     class Meta:
#         unique_together = ['shopping_cart', 'recipe']
#         verbose_name = 'Элемент корзины'
#         verbose_name_plural = 'Элементы корзины'

#     def __str__(self):
#         return f'{self.shopping_cart} - {self.recipe}'
