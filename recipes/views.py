from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView
from django.core.paginator import Paginator
from django.utils.text import slugify
from .models import Post, Comments
from .forms import CommentForm, RecipeForm


class HomePage(View):
    """
    Home page view
    view for Inspiration sections
    """
    def get(self, request):
        """ 
        Get request
        """
        posts = Post.objects.order_by('-published_on')[:4]
        context = {
            "posts": posts,
        }
        return render(request, 'index.html', context)


def searchbar(request):
    """ 
    Search bar view, template form youtube.
    """
    # https://www.youtube.com/watch?v=AGtae4L5BbI
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(title__icontains=searched)
        return render(request, 'searchbar.html',
        {'searched': searched, 'posts': posts})
    else:
        return render(request, 'searchbar.html', {})


class Register(View):
    """
    Register
    """
    template_name = 'register.html'


class RecipeLike(View):
    """
    Recipe_likes
    """
    def post(self, request, slug):
        """
        like and unlike posts
        """
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('recipe_details', args=[slug]))


class AllRecipes(generic.ListView):
    """
    all_recipes view
    """
    model = Post
    queryset = Post.objects.order_by('-published_on')
    template_name = 'all_recipes.html'
    paginate_by = 6


def delete_comment(request, comment_id):
    """
    Deletes comment
    """
    comment = get_object_or_404(Comments, id=comment_id)
    comment.delete()
    return HttpResponseRedirect(reverse(
        'recipe_details', args=[comment.post.slug]))


class EditComment(UpdateView):
    """ 
    Edit Comments 
    """
    model = Comments
    template_name = 'edit_comment.html'
    form_class = CommentForm


class RecipeDetails(View):
    """ 
    Recipe details page
    """
    def get(self, request, slug):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.post_comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_details.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm(),
            }
        )
    def post(self, request, slug):
        """
        What happens when a POST like request
        """
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.post_comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('recipe_details', args=[slug]))
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_details.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )


class YourRecipes(View):

    def get(self, request):
        """
        your_recipes view, get method
        """
        post = Post.objects.filter(author=request.user)
        paginator = Paginator(post, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'your_recipes.html', {"page_obj": page_obj,})


class AddRecipe(View):

    def get(self, request):
        """
        What happens for a GET request
        """
        return render(request, "add_recipe.html", {"recipe_form": RecipeForm()})

    def post(self, request):
        """
        What happens for a POST request
        """
        recipe_form = RecipeForm(request.POST, request.FILES)

        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.slug = slugify('-'.join([recipe.title, str(recipe.author)]), allow_unicode=False)
            recipe.save()
            return redirect('your_recipes')
        else:
            # create message error
            recipe_form = RecipeForm()

        return render(
            request,
            "add_recipe.html",
            {
                 "recipe_form": recipe_form
            },
        )


class EditRecipe(UpdateView):
    """ 
    Edit Recipe 
    """
    model = Post
    template_name = 'edit_recipes.html'
    form_class = RecipeForm


def delete_recipe(request, post_id):
    """
    Deletes recipe
    """
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect(reverse(
        'your_recipes'))


class FavouriteRecipes(View):
    """ favourite recipes view"""
    def get(self, request):
        """favourite_recipes view, get method"""
        if request.user.is_authenticated:
            post = Post.objects.filter(likes=request.user.id)

            paginator = Paginator(post, 6)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(
                request, 'favourite_recipes.html', {"page_obj": page_obj, })
        else:
            return render(request, 'favourite_recipes.html')
