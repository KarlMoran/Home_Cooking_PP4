from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comments

# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('description', 'ingredients', ' preparation_steps')



admin.site.register(Comments)
