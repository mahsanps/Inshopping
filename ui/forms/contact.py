from django.shortcuts import render, redirect
from django import forms
from store.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'title', 'email', 'message')  # Specify the fields to include from the Contact model
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'نام'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
            'title': forms.TextInput(attrs={'placeholder': 'عنوان'}),
            'message': forms.Textarea(attrs={'placeholder': 'پیام خود را بنویسید'}),
        }
        labels = {
            'name': '',
            'email': '',
            'title': '',
            'message': '',
        }