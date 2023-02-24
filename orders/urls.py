from django.urls import path

from .views import (
    OrderDetailView,
    OrderListView,
    CreateOrderView,
    SuccessView,
    CancelView,
    CartView,
    cart_add,
    cart_del,
    cart_clear,
)

app_name = "orders"


urlpatterns = [
    path("cart/", CartView.as_view(), name="cart"),
    path("cart/del/<int:game_id>", cart_del, name="cart_del"),
    path("cart/add/<int:game_id>", cart_add, name="cart_add"),
    path("cart/clear/", cart_clear, name="cart_clear"),
    path("create/", CreateOrderView.as_view(), name="create_order"),
    path("success/", SuccessView.as_view(), name="success_order"),
    path("cancel/", CancelView.as_view(), name="cancel_order"),
    path("", OrderListView.as_view(), name="orders"),
    path("order/<int:pk>", OrderDetailView.as_view(), name="order"),
]
