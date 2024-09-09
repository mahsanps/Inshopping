from store.models import Order
from django.shortcuts import render, redirect
from django import forms

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('delivery_address_state','delivery_address_city','delivery_address_suburb','delivery_address_street_name','delivery_address_unit_number','delivery_address_postcode')
        