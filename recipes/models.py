from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    """
    Post model
    """
    title = models.CharField(max_length=200, unique=True, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')  
    published_on = models.DateField(auto_now_add=True)
    ingredients = models.TextField()
    description = models.TextField()
    preparation_steps = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    comments = models.ManyToManyField(User, related_name='blog_comments', blank= True)  

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

    def number_of_comments(self):
        """
        return comment count
        """
        return self.comments.count()
