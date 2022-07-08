from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import generic, View



# Create your views here.
class Register(View):
    """
    all_recipes view
    """
    template_name='register.html'


class PostList(View):
    """
    Home page view
    """
    def get(self, request):
        """
        get request
        """
        posts = Post.objects.order_by('-published_on')[:4]
        context = {
            "posts": posts,
        }
        return render(request, 'index.html', context)


class AllRecipes(generic.ListView):
    """
    all_recipes view
    """
    model = Post
    queryset = Post.objects.order_by('-published_on')
    template_name = 'all_recipes.html'
    paginate_by = 6

class RecipeDetails(View):
    """ 
    Recipe details page 
    """
    def get(self, request, slug):
        """What happens for a GET request"""
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_details.html",
            {
                "post": post,
                "liked": liked,
            }
        )
