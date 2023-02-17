from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect
from django.views.generic.base import TemplateView

from games.models import Game

from .cart import Cart


class CartView(TemplateView):
    template_name = "orders/cart.html"


def cart_add(request, game_id, update=False):
    cart = Cart(request)
    game = get_object_or_404(Game, id=game_id)
    cart.add(game=game)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def cart_del(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id=game_id)
    cart.remove(game)
    return redirect("orders:cart")
