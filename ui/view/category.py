from django.shortcuts import render, redirect,get_object_or_404
from utils.views import BaseView
from store.models import Category
from store.models import SubCategory


class CategoryPageView(BaseView):
    def get(self, request, *args, **kwargs):
        category_name=kwargs.get("category_name")
        categories = Category.objects.all()
        category = get_object_or_404(Category, name=category_name)
        subcategories = SubCategory.objects.filter(categoryname=category)
        return render(request, 'category.html', {'category': category, 'categories':categories, 'category_name': category_name, 'subcategories': subcategories})

