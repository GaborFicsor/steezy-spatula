from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from multiselectfield import MultiSelectField
from datetime import timedelta


class Recipe(models.Model):
    """
    Recipe object model
    fields:
        -type
        -difficulty
        -author
        -recipe-name
        -ingredients
        -method
        -preparation time
        -cooking time
        -vegan
        -serving size
        -calories per serving
        -slug
        -featured image
        -date of creation
        -date of updating
        -saves
    """
    TYPE = [
        (0, 'Breakfast'),
        (1, 'Lunch'),
        (2, 'Dinner'),
        (3, 'Snack')
    ]
    DURATION = [
        (timedelta(minutes=0), '0 mins'),
        (timedelta(minutes=5), '5 mins'),
        (timedelta(minutes=10), '10 mins'),
        (timedelta(minutes=15), '15 mins'),
        (timedelta(minutes=20), '20 mins'),
        (timedelta(minutes=25), '25 mins'),
        (timedelta(minutes=30), '30 mins'),
        (timedelta(minutes=35), '35 mins'),
        (timedelta(minutes=40), '40 mins'),
        (timedelta(minutes=45), '45 mins'),
        (timedelta(minutes=50), '50 mins'),
        (timedelta(minutes=55), '55mins'),
        (timedelta(minutes=60), '1 hour')
    ]
    DIFFICULTY = [
        (20, 'Easy'),
        (40, 'Moderate'),
        (60, 'Intermediate'),
        (80, 'Challenging')
    ]
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recipe_posts"
    )
    recipe_name = models.CharField(
        max_length=50,
        unique=True,
        null=False,
    )
    type = models.IntegerField(
        choices=TYPE,
        null=False,
    )
    ingredients = models.TextField(null=False)
    method = models.TextField(null=False)
    prep_time = models.DurationField(
        choices=DURATION,
        null=False,
    )
    cooking_time = models.DurationField(
        choices=DURATION,
        null=False,
    )
    vegan = models.BooleanField(default=False)
    serving_size = models.PositiveIntegerField(null=False)
    calories_per_serving = models.PositiveIntegerField(null=False)
    difficulty = models.IntegerField(
        choices=DIFFICULTY,
        null=False,
    )
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    saves = models.ManyToManyField(
        User,
        related_name='recipe_saves',
        blank=True
    )

    class Meta:
        """
        order by creation date, most recent is first
        """
        ordering = ['-created_on']

    def __str__(self):
        return self.recipe_name


class Comment(models.Model):
    """
    Comment object model
    fields:
        -recipe (as foreignkey)
        -name
        -email
        -body
        -date of creation
    credit:
    Code Institute's "I think therefore I blog walkthrough project"
    """
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='comments')
    name = models.CharField(max_length=150)
    email = models.EmailField()
    body = models.TextField(null=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        order by creation date, most recent is at the top
        """
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
