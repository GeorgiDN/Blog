from django.contrib import admin
from WebApp.blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
    list_filter = ('date_posted', 'title')
    search_fields = ('title', 'content', 'date_posted')

