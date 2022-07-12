from django.shortcuts import render, get_object_or_404, reverse
from .models import Post, Comments
from django.views import generic, View
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.views.generic import UpdateView



class HomePage(View):
    """
    Home page view
    view for last added recipes and most loved recipes sections
    """
    def get(self, request):
        """ get request """
        posts = Post.objects.order_by('-published_on')[:4]
        context = {
            "posts": posts,
        }
        return render(request, 'index.html', context)


class Register(View):
    """
    all_recipes view
    """
    template_name='register.html'


class RecipeLike(View):
    """
    Home page view
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
    """Deletes comment"""
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return HttpResponseRedirect(reverse(
        'recipe_details', args=[comment.post.slug]))



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
                "comment": comments,
                "liked": liked,
                "comment_form": CommentForm(),
            }
        )
    def post(self, request, slug):
        """
        What happens for when a POST request
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
                "comment": comments,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )
