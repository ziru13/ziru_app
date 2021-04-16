from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.


def recipe_category(request):
    categories = models.RecipeCategory.objects.all()
    return render(request, 'app/recipe_category.html', {'categories': categories})


# def recipe_list(request):
#     recipes = models.Post.objects.all()
#     return render(request, 'app/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(models.Post, pk=pk)
    return render(request, 'app/recipe_detail.html', {'recipe': recipe})