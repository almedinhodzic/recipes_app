from django.forms import ModelForm

from .models import Category, Recipe


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
