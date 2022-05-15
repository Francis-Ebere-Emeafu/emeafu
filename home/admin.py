from django.contrib import admin

from home.models import BlogAuthor, BlogDetailPage, BlogCategory


@admin.register(BlogAuthor)
class BlogAuthorAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']


@admin.register(BlogDetailPage)
class BlogDetailPageAdmin(admin.ModelAdmin):
    list_display = ['custom_title', 'date']



@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['title']