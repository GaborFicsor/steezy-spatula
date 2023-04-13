from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('recipes/', views.RecipeList.as_view(), name='recipes'),
    path('recipes/<int:pk>', views.RecipeList.as_view(), name='recipes'),
    path('recipes/create', views.RecipeCreateView.as_view(), name='create_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('recipes/edit/<slug:slug>', views.RecipeUpdateView.as_view(), name='update_recipe'),
    path('recipes/<slug:slug>/delete', views.RecipeDeleteView.as_view(), name='delete_recipe'),
    path('<int:pk>', views.CommentUpdateView.as_view(), name='edit_comment'),
    path('<int:pk>/delete', views.CommentDeleteView.as_view(), name='delete_comment'),
    path('profile/<str:username>', views.UserProfileView.as_view(), name='profile'),
    # dashboard
    path('dashboard', views.DashBoardView.as_view(), name='dashboard'),
    # path('dashboard/recipes', views.DashBoardView.as_view(), name='dashboard'),
    # path('dashboard/comments', views.DashBoardView.as_view(), name='dashboard'),


    path('save/<slug:slug>/', views.SaveRecipe.as_view(), name='saved'),

]
