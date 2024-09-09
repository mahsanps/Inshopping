
from django.shortcuts import render, redirect
from django import forms
from store.models import Product


class DeleteProductForm(forms.ModelForm):
    class Meta:
        model = Product  # Specify the model for the form
        fields = [] 