from django.shortcuts import render, redirect,get_object_or_404
from utils.views import BaseView
from store.models import Category
from store.models import SubCategory

class CategoryPageView(BaseView):
    def get(self, request, *args, **kwargs):
        # Fetch the category_slug from the URL kwargs
        category_slug = kwargs.get("category_slug")

        # Fetch all categories for display
        categories = Category.objects.all()

        # Get the category by slug
        category = get_object_or_404(Category, slug=category_slug)

        # Fetch subcategories related to this category using the current field name (categoryname)
        subcategories = SubCategory.objects.filter(categoryname=category)

        # Render the template with the category, categories, and subcategories
        return render(request, 'category.html', {
            'category': category,
            'categories': categories,
            'category_slug': category_slug,
            'subcategories': subcategories
        })
