from store.models import ShopImage
from django.shortcuts import render, redirect
from django import forms



class ShopImagesForm(forms.ModelForm):
     class Meta:
        model = ShopImage
        fields = ('banner_image1', 'banner_image2', 'banner_image3')
        
        def __init__(self, *args, **kwargs):
            super(ShopImagesForm, self).__init__(*args, **kwargs)
            self.fields['banner_image1'].required = False   
            self.fields['banner_image2'].required = False 
            self.fields['banner_image3'].required = False 