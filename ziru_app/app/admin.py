from django.contrib import admin
from .models import RecipeCategory, Post


# Register your models here.
# class RecipeCategoryInline(admin.StackedInline):
#     model = Recipe
# 
# 
# class RecipeAdmin(admin.ModelAdmin):
#     inlines = [RecipeCategoryInline, ]
# 
# 
# class PostInline(admin.StackedInline):
#     model = Post
# 
# 
# class PostAdmin(admin.ModelAdmin):
#     inlines = [PostInline, ]
# 
# 
# admin.site.register(ReceiptCategory, ReceiptAdmin)
# admin.site.register(Recipe)
admin.site.register(RecipeCategory)
admin.site.register(Post)





