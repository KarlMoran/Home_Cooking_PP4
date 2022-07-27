from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))

# Django3blog

class Post(models.Model):
    """
    Post model
    """
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
    related_name ='blog_posts')
    published_on = models.DateField(auto_now_add=True)
    ingredients = models.TextField()
    description = models.TextField()
    preparation_steps = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """
        ordering
        """
        ordering = ['-published_on']

    def __str__(self):
        """
        string title
        """
        return self.title

    def number_of_likes(self):
        """
        return likes count
        """
        return self.likes.count()

    def get_absolute_url(self):
        """
        Absolute URL
        """
        return reverse('your_recipes')

# Django3blog

class Comments(models.Model):
    """
    Comments class
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
    related_name='post_comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    