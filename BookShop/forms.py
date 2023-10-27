from django import forms
from BookShop.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['email','payment_method']