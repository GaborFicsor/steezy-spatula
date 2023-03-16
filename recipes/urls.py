from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeCard.as_view(), name='home')
]
