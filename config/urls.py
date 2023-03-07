from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.cache import cache_page

from games.views import IndexView
from orders.views import CreateOrderView

urlpatterns = [
    path("", cache_page(2)(IndexView.as_view()), name="index"),
    path("admin/", admin.site.urls),
    path("games/", include("games.urls", namespace="games")),
    path("users/", include("users.urls", namespace="users")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("accounts/", include("allauth.urls")),
    path("webhook/stripe/", CreateOrderView.stripe_webhook_view(), name="stripe"),
    path("captcha/", include("captcha.urls")),
    path("api/", include("api.urls")),
]

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
