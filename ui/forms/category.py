from dal import forward
from django import forms
from store.models import Category
from dal import autocomplete


class CategoryForm(forms.Form):
    subcategories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(
            url='subcategory-autocomplete',
            forward=(forward.Self(),)
        )
    )
