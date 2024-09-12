from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),  # List all recipes
    path('add/', views.add_recipe, name='add_recipe'),  # Add a new recipe
    path('edit/<int:pk>/', views.edit_recipe, name='edit_recipe'),  # Edit an existing recipe
    path('delete/<int:pk>/', views.delete_recipe, name='delete_recipe'),  # Delete a recipe
]
