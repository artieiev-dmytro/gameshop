from django.shortcuts import render


def index(request):
    return render(request, "games/index.html")


def games(request):
    return render(request, "games/games.html")
