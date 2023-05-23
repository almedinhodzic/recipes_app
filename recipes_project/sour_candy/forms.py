from django import forms

from .models import Category, Recipe


class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(label='Category', max_length=100)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({"class": "form-select"})