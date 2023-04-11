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
            'main_ingredient',
            'label',
            'ingredients',
            'method',
            'prep_time',
            'cooking_time',
            'nuts',
            'dairy',
            'eggs',
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

class RecipeFilterForm(forms.Form):
    name = forms.CharField()
