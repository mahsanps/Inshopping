from store.models import ProductImage
from django.shortcuts import render, redirect
from django import forms



class ProductsImagesForm(forms.ModelForm):
     class Meta:
        model = ProductImage
        fields = [] 
        