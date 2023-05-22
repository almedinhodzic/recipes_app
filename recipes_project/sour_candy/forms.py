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


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({"class": "form-select"})