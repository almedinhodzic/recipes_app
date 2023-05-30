from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_recipes, name="recipes"),
    path("recipes/", views.get_recipes, name="recipes"),
    path("recipes/create/", views.create_recipe, name="create_recipe"),
    path("recipes/<int:id>/", views.get_recipe, name="get_recipe"),
    path('recipes/update/<int:id>/', views.update_recipe, name="update_recipe"),
    path('recipes/delete/<int:id>/', views.delete_recipe, name="delete_recipe"),
    path('recipes/pdf', views.recipes_pdf, name="recipes_pdf"),
    path('my_recipes/', views.get_my_recipes, name="my_recipes"),
    path('update_profile/', views.update_profile, name="update_profile"),
]
