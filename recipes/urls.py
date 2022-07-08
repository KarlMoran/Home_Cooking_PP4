
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('all_recipes', views.AllRecipes.as_view(), name='all_recipes'),
    path('register', views.Register.as_view(), name='register'),
    path('login', views.LogIn.as_view(), name='login'),
]
