from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RecipeForm, ProfileForm
from .models import Recipe, Profile


def get_recipes(request):
    recipes = Recipe.objects.all().order_by('-updated_at')
    return render(request, 'recipes.html', {'recipes': recipes})


@login_required()
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


@login_required()
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


@login_required
def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes')

    return render(request, 'recipe.html', {'recipe': recipe})


@login_required
def get_my_recipes(request):
    recipes = Recipe.objects.filter(creator=request.user)
    return render(request, 'my_recipes.html', {'recipes': recipes})


def handling_404(request, exception):
    return render(request, '404.html', {})


def update_profile(request):
    form = ProfileForm()
    return render(request, 'my_profile.html', {'form': form})
