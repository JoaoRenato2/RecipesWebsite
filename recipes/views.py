from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(requets):
    return render(requets, 'recipes/pages/home.html')

def recipe(requets,id):
    return render(requets, 'recipes/pages/recipe-view.html')

