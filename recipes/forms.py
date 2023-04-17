from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'recipe_name',
            'type',
            'vegan',
            'nuts',
            'dairy',
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


class SaveForm():
    class Meta:
        model = Recipe
        fields = ('saved',)


class RecipeFilterForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'type', 'difficulty',)

        widgets = {
            'recipe_name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'difficulty': forms.Select(attrs={'class': 'form-control'}),
        }
