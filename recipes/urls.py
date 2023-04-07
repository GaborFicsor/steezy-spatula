from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('recipes/', views.RecipeList.as_view(), name='recipes'),
    path('recipes/create', views.RecipeCreateView.as_view(), name='create_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('recipes/recipe_form_edit/<slug:slug>', views.RecipeUpdateView.as_view(), name='update_recipe'),
]
