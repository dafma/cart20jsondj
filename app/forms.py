from django.forms import ModelForm
from django import forms
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ('user', 'id', 'total_amount')
        fields = ( 'first_name',)