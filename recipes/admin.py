from django.contrib import admin
from .models import Recipe, Comment

from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):

    list_display = (
        'recipe_name',
        'author',
        'type',
        'difficulty',
        'created_on',
        'updated_on'
        )
    search_fields = ['recipe_name', 'method', 'ingredients']
    prepopulated_fields = {'slug': ('recipe_name',)}
    list_filter = ('created_on',)
    summernote_fields = ('method', 'ingredients')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_on',)
    list_filter = ('created_on',)
    search_fields = ('name', 'eamil', 'body')

