from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comments

# Django3blog

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'published_on')
    search_fields = (['title', 'content'])
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'published_on')
    summernote_fields = ('description', 'ingredients', 'preparation_steps')


admin.site.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    search_fields = ('name', 'email', 'body')
