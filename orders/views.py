from django.shortcuts import render, redirect, get_object_or_404

from .cart import Cart
from games.models import Game


def cart(request):
    cart = Cart(request)
    context = {
        "cart": cart,
    }
    return render(request, "orders/cart.html", context)


def cart_add(request, game_id, update=False):
    cart = Cart(request)
    game = get_object_or_404(Game, id=game_id)
    cart.add(game=game)
    return redirect("orders:cart")


def cart_del(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id=game_id)
    cart.remove(game)
    return redirect("orders:cart")
