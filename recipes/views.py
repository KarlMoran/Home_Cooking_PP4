from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post

# Create your views here.
class PostList(TemplateView):
    """
    Home page view
    """
    template_name = 'base.html'

class AllRecipes(TemplateView):
    """
    all_recipes view
    """
    template_name='all_recipes.html'