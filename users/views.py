from django.urls import reverse_lazy, reverse
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView

from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from .models import User, EmailVerification


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
    pass


class EmailVerificationView(TemplateView):
    template_name = "users/email_verification.html"

    def get(self, request, *args, **kwargs):
        user = User.objects.get(email=kwargs["email"])
        email_verification = EmailVerification.objects.filter(
            user=user, code=kwargs["code"]
        )
        if email_verification.exists() and not email_verification.first().is_expirad():
            user.is_verified_email = True
            user.save()
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("index"))
