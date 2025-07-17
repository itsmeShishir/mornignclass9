from django.contrib import admin
from .models import *
# Customized admin panel
# methods and fields
# BASIC -> 
# Register your models here.
# admin.site.register(Category)
# admin.site.register(Tag)
# admin.site.register(Blog)
# admin.site.register(Comment)

# USING modelAdmin class
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'img']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    ordering = ['title']
    # list_editable = ['title']
    # readonly_fields = ['slug']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    ordering = ['title']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'small_content', 'slug', 'img','home_page_show', 
                    'featured_blog', 'category']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    ordering = ['title']
    list_editable = ['home_page_show', 
                     'featured_blog']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'content']
    search_fields = ['user']
    ordering = ['created_at']
