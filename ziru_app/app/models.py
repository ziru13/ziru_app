from django.db import models


class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    recipe_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    # url = models.URLField(max_length=250)
    ingredients = models.TextField()
    instructions = models.TextField()
    notes = models.TextField()

    class Meta:
        ordering = ['created_at', 'updated_at']

    def __str__(self):
        return self.name
