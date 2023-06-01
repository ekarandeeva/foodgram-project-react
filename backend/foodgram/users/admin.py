from django.contrib import admin

from .models import User, Subscription


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'email',
        'first_name',
        'last_name'
    )
    empty_value_display = '-пусто-'
    list_filter = ('username', 'email')
    search_fields = ('username', 'email', 'first_name', 'last_name')


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'author'
    )
    empty_value_display = '-пусто-'
    list_filter = ('user', 'author')
    search_fields = ('user', 'author')


admin.site.register(User, UserAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
