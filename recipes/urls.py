from . import views
from django.urls import path

urlpatterns = [
    # homepage url
    path('', views.HomeView.as_view(), name='homepage'),

    # all recipes list view
    path('recipes/', views.RecipeList.as_view(), name='recipes'),

    # crud views for recipe model
    path('recipes/create',
         views.RecipeCreateView.as_view(), name='create_recipe'),

    path('recipes/<slug:slug>/',
         views.RecipeDetail.as_view(), name='recipe_detail'),

    path('recipes/edit/<slug:slug>',
         views.RecipeUpdateView.as_view(), name='update_recipe'),

    path('recipes/delete/<slug:slug>',
         views.RecipeDeleteView.as_view(), name='delete_recipe'),

    # crud views for comment model
    path('comment/<int:pk>',
         views.CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/delete/<int:pk>',
         views.CommentDeleteView.as_view(), name='delete_comment'),

    # profile views
    path('profile/<str:username>',
         views.UserProfileView.as_view(), name='profile'),
    path('save/<slug:slug>/',
         views.SaveRecipe.as_view(), name='saved'),
]
