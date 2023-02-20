from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter first name"}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter last name"}
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter your email address"}
        )
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your address"}
        )
    )

    class Meta:
        model = Order
        fields = ("first_name", "last_name", "email", "address")
