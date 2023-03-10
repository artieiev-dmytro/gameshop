from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
)
from captcha.fields import CaptchaField
from .tasks import send_email_verification
from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter password"})
    )

    class Meta:
        model = User
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control py4"


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter first name"})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter last name"})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter username"})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email address"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter password"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm the password"})
    )
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control py4"

    def save(self, commit=True):
        user = super().save(commit)
        send_email_verification.delay(user.id)
        return user


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"readonly": True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"readonly": True}))
    image = forms.ImageField(widget=forms.FileInput(attrs={}), required=False)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "image")

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control py4"
        self.fields["image"].widget.attrs["class"] = "custom-file-input"
