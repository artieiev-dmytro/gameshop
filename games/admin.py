from django.contrib import admin

from .models import Developer, Game, Genre


@admin.register(Game)
class AdminGame(admin.ModelAdmin):
    list_display = ("name", "price", "view", "stripe_game_price_id")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Developer)
class AdminDeveloper(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    ordering = ("title",)
