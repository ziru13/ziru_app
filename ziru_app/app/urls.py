from django.urls import path
from . import views


app_name = 'sleepyfish'

urlpatterns = [
    path('categories/', views.recipe_category, name='recipe_category'),
]