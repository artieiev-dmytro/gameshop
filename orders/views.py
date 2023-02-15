from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateView

from .cart import Cart
from games.models import Game


class CartView(TemplateView):
    template_name = "orders/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart"] = Cart(self.request)
        return context


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
