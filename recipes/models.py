from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from multiselectfield import MultiSelectField
from datetime import timedelta


STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    TYPE = [
        (0, 'Breakfast'),
        (1, 'Lunch'),
        (2, 'Dinner'),
        (3, 'Snack')
    ]
    MAIN_INGREDIENT = [
        (0, 'Chicken'),
        (1, 'Noodles'),
        (2, 'Fish'),
        (3, 'Beef'),
        (4, 'Fruit'),
        (5, 'Pork'),
        (6, 'Rice'),
        (7, 'Seafood'),
        (8, 'Potato'),
        (9, 'Bread'),
        (10, 'Vegetables'),
        (11, 'Eggs'),
        (12, 'Oats')
    ]
    LABEL = [
        (0, 'None'),
        (1, 'Vegan'),
        (2, 'Vegetarian'),
    ]
    DURATION = [
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
        (0, 'Easy-peasy'),
        (1, 'I know cooking'),
        (2, 'Up for a challenge'),
        (3, 'Battle hardened')
    ]
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recipe_posts"
    )
    recipe_name = models.CharField(
        max_length=150,
        unique=True,
        null=False,
        default=None
    )
    type = models.IntegerField(
        choices=TYPE,
        null=False,
        default=None
    )
    main_ingredient = models.IntegerField(
        choices=MAIN_INGREDIENT,
        null=False,
        default=None
    )
    label = models.IntegerField(
        choices=LABEL,
        null=False,
        default=None)
    ingredients = models.TextField(null=False, default='')
    method = models.TextField()
    prep_time = models.DurationField(
        choices=DURATION,
        null=False,
        default=None
    )
    cooking_time = models.DurationField(
        choices=DURATION,
        null=False,
        default=None
    )
    nuts = models.BooleanField(default=False)
    dairy = models.BooleanField(default=False)
    eggs = models.BooleanField(default=False)
    serving_size = models.IntegerField()
    calories_per_serving = models.IntegerField()
    difficulty = models.IntegerField(
        choices=DIFFICULTY,
        null=False,
        default=None
    )
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User,
        related_name='recipe_likes',
        blank=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.recipe_name

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='comments')
    name = models.CharField(max_length=150)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
