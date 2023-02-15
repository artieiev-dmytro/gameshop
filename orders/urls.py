from django.urls import path

from .views import CartView, cart_add, cart_del

app_name = "orders"


urlpatterns = [
    path("cart/", CartView.as_view(), name="cart"),
    path("cart/del/<int:game_id>", cart_del, name="cart_del"),
    path("cart/add/<int:game_id>", cart_add, name="cart_add"),
]
