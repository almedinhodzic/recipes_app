from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RecipeForm, CategoryForm

from .models import Category, Recipe


def test(request):
    return render(request, 'test.html', {'test': 'test from the view'})


def get_recipes(request):
    recipes = Recipe.objects.all().order_by('-updated_at')
    return render(request, 'recipes.html', {'recipes': recipes})


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save(commit=True)
            return redirect("recipes")
    else:
        form = RecipeForm()

    return render(request, 'create_recipe.html', {'form': form})


def get_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipe.html', {"recipe": recipe})