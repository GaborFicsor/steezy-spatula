from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('recipes/', views.RecipeList.as_view(), name='recipes'),
    path('recipes/create', views.RecipeCreateView.as_view(), name='create_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]
