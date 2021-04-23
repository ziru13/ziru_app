from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from . import forms
from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.


def recipe_category(request):
    categories = models.Category.objects.all()
    return render(request, 'app/recipe_category.html', {'categories': categories})


def get_a_category(request, category_pk):
    category = get_object_or_404(models.Category, pk=category_pk)
    posts = models.Post.objects.filter(recipe_category_id=category_pk)
    return render(request, 'app/get_a_category.html', {'posts': posts,
                                                       'category': category})


def post_detail(request, category_pk, post_pk):
    post = get_object_or_404(models.Post, pk=post_pk)
    return render(request, 'app/post_detail.html', {'post': post})


def newest_post(request):
    """Get the 5 newest posts"""
    posts = get_object_or_404(models.Post).order_by('-created_at')[:5]
    return render(request, 'home.html', {'posts': posts})

@login_required
def post_create(request, category_pk):
    category = get_object_or_404(models.Category, pk=category_pk)
    form = forms.PostForm()   # 一个空的form

    if request.method == 'POST':
        form = forms.PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)  # form有效就做一个post
            post.recipe_category = category  # 然后要做跟category相关联
            post.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Post added!')
            return HttpResponseRedirect(post.get_absolute_url())
    return render(request, 'app/post_form.html', {'form': form,
                                                  'category': category})