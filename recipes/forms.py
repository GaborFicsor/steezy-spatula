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
        labels = {
            'body': 'max 300 characters'
        }

    def clean_body(self):
        body = self.cleaned_data.get('body')
        if len(body) >= 300:
            raise forms.ValidationError('Your comment is too long')
        return body


class RecipeForm(forms.ModelForm):
    """
    credit:
    https://github.com/summernote/django-summernote
    form validators:
    https://www.youtube.com/watch?v=yFGj4ZDbiiE
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
        labels = {
            'recipe_name': 'Recipe Name',
            'type': 'Recipe Type',
            'vegan': 'Is this recipe vegan?',
            'ingredients': 'Ingredients(max 1500 characters)',
            'method': 'Method(max 4000 characters)',
            'prep_time': 'Preparation Time',
            'cooking_time': 'Cooking Time',
            'serving_size': 'Serving Size',
            'calories_per_serving': 'Calories Per Serving',
            'difficulty': 'Difficulty',
            'featured_image': 'Image(not required)'
        }

    def clean_serving_size(self):
        serving_size = self.cleaned_data.get('serving_size')
        if serving_size == 0:
            raise forms.ValidationError('Serving size can not be 0')
        elif serving_size > 99:
            raise forms.ValidationError(
                'Please enter a realistic serving size (1-99)')
        return serving_size

    def clean_calories_per_serving(self):
        calories_per_serving = self.cleaned_data.get('calories_per_serving')
        if calories_per_serving == 0:
            raise forms.ValidationError('The amount of calories can not be 0')
        elif calories_per_serving < 50 or calories_per_serving > 5000:
            raise forms.ValidationError(
                'Please enter a realistic amount of calories (50-5000)')
        return calories_per_serving

    def clean_ingredients(self):
        ingredients = self.cleaned_data.get('ingredients')
        if len(ingredients) >= 1500:
            raise forms.ValidationError(
                'Please try adding a shorter description for the ingredients')
        return ingredients

    def clean_method(self):
        method = self.cleaned_data.get('method')
        if len(method) >= 4000:
            raise forms.ValidationError(
                'Please try adding a shorter description for the method')
        return method


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
