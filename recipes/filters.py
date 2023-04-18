import django_filters
from .models import Recipe
from django import template

register = template.Library()


class RecipeFilter(django_filters.FilterSet):
    """
    filter for recipe model, filterform rendered on recipes.html
    """
    recipe_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Recipe
        fields = {
            'recipe_name',
            'type',
            'difficulty',
            'vegan'
        }
