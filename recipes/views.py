from django.shortcuts import render
from utils.recipes.factory import make_recipe

# Create your views here.
def home(requets):
    return render(requets, 'recipes/pages/home.html',context={'recipes':[make_recipe() for _ in range(10)],})

def recipe(requets,id):
    return render(requets, 'recipes/pages/recipe-view.html', context={'recipe':make_recipe(),})

