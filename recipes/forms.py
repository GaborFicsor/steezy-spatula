from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    """
    credit:
    Code Institute's "I think therefore I blog walkthrough project"
    """
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """
    credit:
    https://github.com/summernote/django-summernote
    """
    class Meta:
        model = Recipe
        fields = (
            'recipe_name',
            'type',
            'vegan',
            'ingredients',
            'method',
            'prep_time',
            'cooking_time',
            'serving_size',
            'calories_per_serving',
            'difficulty',
            'featured_image',
        )
        widgets = {
            'ingredients': SummernoteWidget(),
            'method': SummernoteWidget(),
        }


class RecipeFilterForm(forms.ModelForm):
    """
    credit:
    https://www.youtube.com/watch?v=6-XXvUENY_8
    """
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'type', 'difficulty', 'vegan')

        widgets = {
            'recipe_name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'difficulty': forms.Select(attrs={'class': 'form-control'}),
            'vegan': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
