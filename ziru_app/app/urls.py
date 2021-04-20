from django.urls import path
from . import views


app_name = 'sleepyfish'

urlpatterns = [
    path('recipes/', views.recipe_category, name='recipe_category'),
    path('recipes/<int:category_pk>/<int:post_pk>/', views.post_detail, name='post_detail'),
    path('recipes/<int:category_pk>/create_post/', views.post_create, name='post_create'),
    path('recipes/<int:category_pk>/', views.get_a_category, name='get_a_category'),
]