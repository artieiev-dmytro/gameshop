from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from .models import Developer, Game, Genre


class IndexView(TemplateView):
    template_name = "games/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "GameShop"
        return context


class GamesListView(ListView):
    model = Game
    template_name = "games/games.html"
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        genre_id = self.kwargs.get("genre_id")
        developer_id = self.kwargs.get("developer_id")
        if genre_id:
            return [game for game in queryset.all() if game.genre.filter(id=genre_id)]
        elif developer_id:
            return queryset.filter(developer_id=developer_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genre"] = Genre.objects.all()
        context["developers"] = Developer.objects.all()
        return context
