import stripe
from http import HTTPStatus

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from games.models import Game
from .forms import OrderForm
from .models import Order

from .cart import Cart

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(View):
    def get(self, request):
        cart_clear(request)
        messages.success(request, "You have successfully created order")
        return HttpResponseRedirect(reverse("games:games"))


class CancelView(TemplateView):
    template_name = "orders/cancel.html"


class OrderDetailView(DetailView):
    template_name = "orders/order.html"
    model = Order


class OrderListView(ListView):
    template_name = "orders/orders.html"
    model = Order

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(initiator=self.request.user)


class CreateOrderView(CreateView):
    template_name = "orders/create_order.html"
    form_class = OrderForm
    success_url = reverse_lazy("orders:create_order")

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        cart = Cart(self.request)
        CreateOrderView.cart = cart
        CreateOrderView.order_id = self.object.id
        line_items = []
        for game in cart:
            item = {
                "price": game["game"].stripe_game_price_id,
                "quantity": game["quantity"],
            }
            line_items.append(item)
        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            mode="payment",
            success_url="{}{}".format(
                settings.DOMAIN_NAME, reverse("orders:success_order")
            ),
            cancel_url="{}{}".format(
                settings.DOMAIN_NAME, reverse("orders:cancel_order")
            ),
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super().form_valid(form)

    @classmethod
    def stripe_webhook_view(cls, *args, **kwargs):
        @csrf_exempt
        def wrapper(request):
            payload = request.body
            sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
            event = None

            try:
                event = stripe.Webhook.construct_event(
                    payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
                )
            except ValueError:
                # Invalid payload
                return HttpResponse(status=400)
            except stripe.error.SignatureVerificationError:
                # Invalid signature
                return HttpResponse(status=400)

            # Handle the checkout.session.completed event
            if event["type"] == "checkout.session.completed":
                # Fulfill the purchase...
                CreateOrderView._fulfill_order()

            # Passed signature verification
            return HttpResponse(status=200)

        return wrapper

    @staticmethod
    def _fulfill_order():
        cart = CreateOrderView.cart
        cart_history = {
            "total_sum": float(cart.get_total_price()),
            "purchased_items": cart.convert_json(),
        }
        order = Order.objects.get(id=CreateOrderView.order_id)
        order.update_after_payment(cart_history)


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


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("games:games")
