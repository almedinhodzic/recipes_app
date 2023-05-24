from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RecipeForm, CategoryForm
from django.urls import reverse

from .models import Category, Recipe


def test(request):
    return render(request, 'test.html', {'test': 'test from the view'})


def get_recipes(request):
    recipes = Recipe.objects.all().order_by('-updated_at')
    return render(request, 'recipes.html', {'recipes': recipes})


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect("recipes")
    else:
        form = RecipeForm()

    return render(request, 'create_recipe.html', {'form': form})


def get_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipe.html', {"recipe": recipe})


def update_recipe(request, id):
    recipe = Recipe.objects.get(id=id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('get_recipe', id=id)
    else:
        form = RecipeForm(instance=recipe)
    
    return render(request, 'update-recipe.html', {'form': form, 'id': recipe.id})


def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes')
    
    return render(request, 'recipes.html', {'recipe': recipe})