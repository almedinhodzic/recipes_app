from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RecipeForm, CategoryForm

from .models import Category, Recipe


def get_recipes(request):
    recipes = Recipe.objects.all().order_by('-updated_at')
    return render(request, 'recipes.html', {'recipes': recipes})


@login_required(login_url='/users/login_user')
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.creator = request.user
            recipe.save()
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

    return render(request, 'recipe.html', {'recipe': recipe})


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes')
    else:
        form = CategoryForm()
    return render(request, 'create-category.html', {'form': form})


def get_categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def get_category(request, id):
    category = Category.objects.get(id=id)
    return render(request, 'category.html', {'category': category})


def delete_category(request, id):
    category = Category.objects.get(id=id)

    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category successfully deleted.')
        return redirect('get_categories')

    return render(request, 'delete_category.html', {'category': category})


def update_category(request, id):
    category = Category.objects.get(id=id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('get_categories')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'update_category.html', {'form': form, 'category': category})
