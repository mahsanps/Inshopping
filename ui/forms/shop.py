from store.models import Shop
from django.shortcuts import render, redirect
from django import forms

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('store_name', 'description', 'instagramId', 'email', 'contact', 'address','image')

    def __init__(self, *args, **kwargs):
        super(ShopForm, self).__init__(*args, **kwargs)
        self.fields['store_name'].required = True
        self.fields['description'].required = False
        self.fields['instagramId'].required = True
        self.fields['email'].required = False
        self.fields['contact'].required = False
        self.fields['address'].required = False
        self.fields['image'].required = True