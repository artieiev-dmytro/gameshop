from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (
    EmailVerificationView,
    UserLoginView,
    UserLogoutView,
    UserProfileView,
    UserRegistrationView,
)

app_name = "users"


urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("profile/<int:pk>", login_required(UserProfileView.as_view()), name="profile"),
    path("logout/", login_required(UserLogoutView.as_view()), name="logout"),
    path(
        "varify/<str:email>/<uuid:code>", EmailVerificationView.as_view(), name="varify"
    ),
]
