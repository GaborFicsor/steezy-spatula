from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Ingredient(models.Model):
    INGREDIENTS = (
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
    ingredient_name = models.CharField(choices=INGREDIENTS)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients',
        )


class Allergens(models.Model):
    ALLERGENS = (
        ('Vegan', 'Vegan'),
        ('Vegetarian', 'Vegetarian'),
        ('Gluten-free', 'Gluten-free'),
        ('Contains nuts', 'Contains nuts')
    )
    allergen = models.CharField(choices=ALLERGENS)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='allergens'
        )


class Recipe(models.Model):
    TYPE = (
        (0, 'Breakfast'),
        (1, 'Lunch'),
        (2, 'Dinner'),
        (3, 'Snack')
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
    ingredients = models.ManyToManyField(Ingredient)
    type = models.IntegerField(choices=TYPE)
    method = models.TextField()
    serving_size = models.IntegerField()
    allergens = models.CharField(choices=ALLERGENS)
    calories_per_serving = models.IntegerField()
    difficulty = models.IntegerField(choices=DIFFICULTY)
    prep_time = models.IntegerField()
    cooking_time = models.IntegerField()
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
