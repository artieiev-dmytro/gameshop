from django.urls import path

from .views import cart, cart_add, cart_del

app_name = "orders"


urlpatterns = [
    path("cart/", cart, name="cart"),
    path("cart/del/<int:game_id>", cart_del, name="cart_del"),
    path("cart/add/<int:game_id>", cart_add, name="cart_add"),
]
