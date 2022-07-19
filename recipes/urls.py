from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('all_recipes', views.AllRecipes.as_view(), name='all_recipes'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name="recipe_details"),
    path('like/<slug:slug>', login_required(views.RecipeLike.as_view()), name='recipe_like'),
    path('delete_comment/<int:comment_id>', login_required(views.delete_comment), name='delete_comment'),
    path('edit_comment/<int:pk>', login_required(views.EditComment.as_view()), name='edit_comment'),
    path('your_recipes', login_required(views.YourRecipes.as_view()), name='your_recipes'),
    path('add_recipe', login_required(views.AddRecipe.as_view()), name='add_recipe'),
    path('edit_recipes/<int:pk>', login_required(views.EditRecipe.as_view()), name='edit_recipes'),
    path('delete_recipe/<int:post_id>', login_required(views.delete_recipe), name='delete_recipe'),
    path('favourite_recipes', login_required(views.FavouriteRecipes.as_view()), name='favourite_recipes'),
    path('searchbar', views.searchbar, name='searchbar'),
]