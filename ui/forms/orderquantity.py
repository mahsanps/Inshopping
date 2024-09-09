from store.models import Product
from django.shortcuts import render, redirect
from django import forms

class QuantityOrderForm(forms.Form):
    quantity = forms.IntegerField()
