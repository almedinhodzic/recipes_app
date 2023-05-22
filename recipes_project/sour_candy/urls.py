from django.urls import path
from . import views

urlpatterns = [
    path("", views.test, name="test"),
    path("recipes/", views.get_recipes, name="recipes"),
    path("recipes/create/", views.create_recipe, name="create_recipe"),
    path("recipes/<int:id>/", views.get_recipe, name="get_recipe")
]
