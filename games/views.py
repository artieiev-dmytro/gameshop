from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Game, Genre, Developer


def index(request):
    return render(request, "games/index.html")


def games(request, genre_id=None, developer_id=None, page=1):
    context = {
        "genre": Genre.objects.all(),
        "developers": Developer.objects.all(),
    }
    if genre_id:
        games = [game for game in Game.objects.all() if game.genre.filter(id=genre_id)]
    elif developer_id:
        games = Game.objects.filter(developer_id=developer_id)
    else:
        games = Game.objects.all()

    paginator = Paginator(games, 2)
    games_paginator = paginator.page(page)
    context.update({"games": games_paginator})
    return render(request, "games/games.html", context)
