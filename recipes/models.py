from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    TYPE = (
        (0, 'Breakfast'),
        (1, 'Lunch'),
        (2, 'Dinner'),
        (3, 'Snack')
    )
    DURATION = (
        (5, '5 mins'),
        (10, '10 mins'),
        (15, '15 mins'),
        (20, '20 mins'),
        (25, '25 mins'),
        (30, '30 mins'),
        (35, '35 mins'),
        (40, '40 mins'),
        (45, '45 mins'),
        (50, '50 mins'),
        (55, '55mins'),
        (60, '1 hour')
    )
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
    method = models.TextField()
    ingredients = models.TextField(null=True, default='')
    cooking_time = models.DurationField(choices=DURATION, null=True)
    prep_time = models.DurationField(choices=DURATION, null=True)
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
        ('Eggs', 'Eggs')
    )
    main_ingredient_name = models.CharField(
        max_length=50,
        choices=MAIN_INGREDIENT)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='main_ingredient',
        )


class Allergens(models.Model):
    ALLERGENS = (
        ('Vegan', 'Vegan'),
        ('Vegetarian', 'Vegetarian'),
        ('Gluten-free', 'Gluten-free'),
        ('Contains nuts', 'Contains nuts')
    )
    allergen = models.CharField(max_length=50, choices=ALLERGENS)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='allergens'
        )


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
