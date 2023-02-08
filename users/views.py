from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegisterForm, UserProfileForm


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("games:games"))
    else:
        form = UserLoginForm()
    context = {"form": form}
    return render(request, "users/login.html", context)


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully registered!")
            return HttpResponseRedirect(reverse("users:login"))
    else:
        form = UserRegisterForm()
    context = {"form": form}
    return render(request, "users/register.html", context)


@login_required()
def profile_view(request):
    if request.method == "POST":
        form = UserProfileForm(
            data=request.POST, instance=request.user, files=request.FILES
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:profile"))
    else:
        form = UserProfileForm(instance=request.user)
    context = {"form": form}
    return render(request, "users/profile.html", context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("games:games"))
