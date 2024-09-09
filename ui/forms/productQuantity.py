from store.models import ProductVariation, Product
from django.shortcuts import render, redirect
from django import forms

class ProductsQuantityForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(),required=False)
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput(),required=False)
    class Meta:
        model = ProductVariation
        fields = ('size','color', 'quantity')
         
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget = forms.HiddenInput()  # Set the id field widget to HiddenInput
        self.fields['id'].disabled = True 
        self.fields['color'].required = False
        self.fields['size'].required = False
        self.fields['quantity'].required = True