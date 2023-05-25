from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_recipes, name="recipes"),
    path("recipes/", views.get_recipes, name="recipes"),
    path("recipes/create/", views.create_recipe, name="create_recipe"),
    path("recipes/<int:id>/", views.get_recipe, name="get_recipe"),
    path('recipes/update/<int:id>/', views.update_recipe, name="update_recipe"),
    path('recipes/delete/<int:id>/', views.delete_recipe, name="delete_recipe"),
    path('categories/', views.get_categories, name="get_categories"),
    path('categories/delete/<int:id>/', views.delete_category, name="delete_category"),
    path('categories/update/<int:id>/', views.update_category, name="update_category"),
]
