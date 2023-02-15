from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView

from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from .models import User


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm


class UserRegistrationView(SuccessMessageMixin, CreateView):
    model = User
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")
    success_message = "You have successfully registered"


class UserProfileView(UpdateView):
    model = User
    template_name = "users/profile.html"
    form_class = UserProfileForm

    def get_success_url(self):
        return reverse_lazy("users:profile", args=(self.object.id,))


class UserLogoutView(LogoutView):
    success_url = reverse_lazy("games:games")
