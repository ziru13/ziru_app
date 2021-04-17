from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.


def recipe_category(request):
    categories = models.Category.objects.all()
    return render(request, 'app/recipe_category.html', {'categories': categories})


def get_a_category(request, category_pk):
    posts = models.Post.objects.filter(recipe_category_id=category_pk)
    return render(request, 'app/get_a_category.html', {'posts': posts})


def post_detail(request, category_pk, post_pk):
    post = get_object_or_404(models.Post, recipe_category_id=category_pk,pk=post_pk)
    return render(request, 'app/post_detail.html', {'post': post})
