from django.shortcuts import render
from store.models import Category, Shop, Product

# Create your views here.
def facebook_login(request):
    return render(request, "facebook_login.html", {})
    