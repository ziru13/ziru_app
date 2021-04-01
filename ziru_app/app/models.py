from django.db import models


# Create your models here.
# class Recipe(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     name = models.CharField(max_length=255)
# 
#     def __str__(self):
#         return self.name
# 
#     class Meta:
#         ordering = ['created_at']
#         verbose_name_plural = 'recipes'


class RecipeCategory(models.Model):
    # recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Recipe-Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    # recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipe_category = models.ForeignKey(RecipeCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=250)
    ingredients = models.TextField()
    instructions = models.TextField()
    notes = models.TextField()

    class Meta:
        ordering = ['created_at', 'updated_at']

    def __str__(self):
        return self.name
