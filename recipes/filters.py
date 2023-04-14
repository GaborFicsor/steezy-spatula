import django_filters
from .models import Recipe
from django import template

register = template.Library()

class RecipeFilter(django_filters.FilterSet):
    class Meta:
        model = Recipe
        fields = {
            'recipe_name': ['icontains'],
            'type': ['exact'],
            'difficulty': ['exact'],
            'label': ['exact']
        }

