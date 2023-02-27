from django.contrib import admin

from .models import Developer, Game, Genre, Comment


class CommentInstanceInline(admin.TabularInline):
    model = Comment


@admin.register(Game)
class AdminGame(admin.ModelAdmin):
    list_display = ("name", "price", "view", "stripe_game_price_id")
    search_fields = ("name",)
    ordering = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [CommentInstanceInline]


@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Developer)
class AdminDeveloper(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    ordering = ("title",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Comment)
