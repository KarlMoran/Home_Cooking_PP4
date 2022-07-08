from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post

# Create your views here.
class Register(TemplateView):
    """
    all_recipes view
    """
    template_name='register.html'


class PostList(TemplateView):
    """
    Home page view
    """
    template_name = 'index.html'

class AllRecipes(TemplateView):
    """
    all_recipes view
    """
    template_name='all_recipes.html'

class LogIn(TemplateView):
    """
    all_recipes view
    """
    template_name='login.html'