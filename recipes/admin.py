from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comments

# Register your models here.
admin.site.register(Post)
admin.site.register(Comments)
