from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from multiselectfield import MultiSelectField
from datetime import timedelta


STATUS = ((0, "Draft"), (1, "Published"))


class MainIngredient(models.Model):
    MAIN_INGREDIENT = (
        ('Chicken', 'Chicken'),
        ('Noodles', 'Noodles'),
        ('Fish', 'Fish'),
        ('Beef', 'Beef'),
        ('Fruit', 'Fruit'),
        ('Pork', 'Pork'),
        ('Rice', 'Rice'),
        ('Seafood', 'Seafood'),
        ('Potato', 'Potato'),
        ('Bread', 'Bread'),
        ('Vegetables', 'Vegetables'),
        ('Eggs', 'Eggs'),
        ('Oats', 'Oats')
    )
    main_ingredient_name = models.CharField(
        max_length=50,
        choices=MAIN_INGREDIENT)


class Allergens(models.Model):
    ALLERGENS = (
        ('None', 'None'),
        ('Vegan', 'Vegan'),
        ('Vegetarian', 'Vegetarian'),
        ('Gluten-free', 'Gluten-free'),
        ('Contains nuts', 'Contains nuts'),
        ('Dairy-free', 'Dairy-free'),
    )
    allergen = models.CharField(max_length=50, choices=ALLERGENS)


class Recipe(models.Model):
    TYPE = (
        (0, 'Breakfast'),
        (1, 'Lunch'),
        (2, 'Dinner'),
        (3, 'Snack')
    )

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
    DIFFICULTY = (
        (0, 'Easy-peasy'),
        (1, 'I know cooking'),
        (2, 'Up for a challenge'),
        (3, 'Battle hardened')
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recipe_posts")
    recipe_name = models.CharField(max_length=150, unique=True)
    type = models.IntegerField(choices=TYPE)
    main_ingredient = models.ManyToManyField(
        MainIngredient,
        choices=MainIngredient.MAIN_INGREDIENT)
    allergens = models.ManyToManyField(
        Allergens,
        choices=Allergens.ALLERGENS,
        default='None')
    ingredients = models.TextField(null=False, default='')
    method = models.TextField()
    prep_time = models.DurationField(
        choices=DURATION,
        null=False,
        default=(timedelta(minutes=15), '15 mins'))
    cooking_time = models.DurationField(
        choices=DURATION,
        null=False,
        default=(timedelta(minutes=30), '30 mins'))
    serving_size = models.IntegerField()
    calories_per_serving = models.IntegerField()
    difficulty = models.IntegerField(choices=DIFFICULTY)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User,
        related_name='recipe_likes',
        blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

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
