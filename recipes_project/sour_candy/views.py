from django.http import HttpResponse
from django.shortcuts import render
from .forms import RecipeForm, CategoryForm

from .models import Category, Recipe


def test(request):
    return render(request, 'test.html', {'test': 'test from the view'})


def get_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': recipes})


def create_recipe(request):
    form = RecipeForm()
    return render(request, 'create_recipe.html', {'form': form})


def get_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipe.html', {"recipe": recipe})