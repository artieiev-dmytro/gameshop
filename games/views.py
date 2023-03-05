from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.cache import cache
from django.shortcuts import redirect


from .models import Developer, Game, Genre, Rating, Comment
from .forms import CommentForm
from common.mixins import TitleMixin


class IndexView(TemplateView):
    template_name = "games/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "GameShop"
        return context


class GameDetailView(TitleMixin, DetailView):
    template_name = "games/game_detail.html"
    model = Game

    def get_context_data(self, **kwargs):
        self.title = self.object.name
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["rating"] = self.get_rating()
        context["comments"] = Comment.objects.filter(game__id=self.object.id)
        genre = cache.get("genre")
        developers = cache.get("developers")
        if not genre:
            context["genre"] = Genre.objects.all()
            cache.set("genre", context["genre"], 60)
        else:
            context["genre"] = genre

        if not developers:
            context["developers"] = Developer.objects.all()
            cache.set("developers", context["developers"], 60)
        else:
            context["developers"] = developers
        return context

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, *kwargs)
        obj.plus_view()
        return obj

    def get_rating(self):
        ratings = Rating.objects.filter(game__id=self.object.id)
        if not ratings:
            return 0.0
        res = round(sum(map(lambda obj: obj.rating, ratings)) / len(ratings), 1)
        return res


class GamesListView(TitleMixin, ListView):
    model = Game
    template_name = "games/games.html"
    paginate_by = 1
    title = "Catalog"

    def get_queryset(self):
        queryset = super().get_queryset()
        genre_slug = self.kwargs.get("slug_genre")
        developer_slug = self.kwargs.get("slug_developer")
        if genre_slug:
            return [
                game for game in queryset.all() if game.genre.filter(slug=genre_slug)
            ]
        elif developer_slug:
            return queryset.filter(developer__slug=developer_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = cache.get("genre")
        developers = cache.get("developers")
        if not genre:
            context["genre"] = Genre.objects.all()
            cache.set("genre", context["genre"], 60)
        else:
            context["genre"] = genre

        if not developers:
            context["developers"] = Developer.objects.all()
            cache.set("developers", context["developers"], 60)
        else:
            context["developers"] = developers
        return context


def rating(request, game_id):
    rating = Rating.objects.filter(user__id=request.user.id, game__id=game_id)
    if not rating:
        Rating.objects.create(user=request.user, game=Game(id=game_id))
    rating.first().update_rating(int(request.POST.get("rating")))
    return redirect(request.META.get("HTTP_REFERER"))


def create_comment(request, game_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.game = Game.objects.get(id=game_id)
            comment.save()
    return redirect(request.META.get("HTTP_REFERER"))


class SearchView(GamesListView):
    def get_queryset(self):
        return Game.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f"q={self.request.GET.get('q')}&"
        return context
