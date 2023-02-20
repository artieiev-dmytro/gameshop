from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from games.models import Game
from .forms import OrderForm

from .cart import Cart


class CreateOrderView(CreateView):
    template_name = "orders/create_order.html"
    form_class = OrderForm


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
