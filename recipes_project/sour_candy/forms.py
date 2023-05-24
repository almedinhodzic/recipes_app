from django import forms

from .models import Category, Recipe


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({"class": "form-select"})