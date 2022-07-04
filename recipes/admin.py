from .models import Category, Recipe
from django.contrib import admin

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...
    
