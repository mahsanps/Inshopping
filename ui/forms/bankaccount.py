from store.models import BankAccount
from django.shortcuts import render, redirect
from django import forms

class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ('name', 'bankName', 'cartNumber','accountNumber')