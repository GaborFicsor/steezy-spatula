import django_filters
from .models import Recipe
from django import template

register = template.Library()


class RecipeFilter(django_filters.FilterSet):
    """
    filter for recipe model, filterform rendered on recipes.html
    credit:
    https://django-filter.readthedocs.io/en/stable/guide/usage.html
    https://stackoverflow.com/questions/65158059/django-filters-icontains-type-of-lookup-expression-doesnt-work-properly
    https://www.youtube.com/watch?v=FTUxl5ZCMb8
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
