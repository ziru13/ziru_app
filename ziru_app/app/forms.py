from django import forms

from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = [
            'recipe_category',
            'name',
            'description',
            'ingredients',
            'instructions',
            'notes', ]