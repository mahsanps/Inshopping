from store.models import ShopImage
from django.shortcuts import render, redirect
from django import forms



class ShopImagesForm(forms.ModelForm):
     class Meta:
        model = ShopImage
        fields = ('banner_image1', 'banner_image2', 'banner_image3')