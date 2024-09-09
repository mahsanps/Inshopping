from store.models import OrderDelivery, Order
from django.shortcuts import render, redirect
from django import forms

class OrderDeliveryForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(),required=False)
    order = forms.ModelChoiceField(queryset=Order.objects.all(), widget=forms.HiddenInput(),required=False)
    class Meta:
        model = OrderDelivery
        fields =['status','tracking_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget = forms.HiddenInput()  # Set the id field widget to HiddenInput
        self.fields['id'].disabled = True 
        self.fields['status'].required = False
        self.fields['tracking_number'].required = False