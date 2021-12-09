from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    servings = models.IntegerField()
    ingredients = models.TextField()
    instructions = models.TextField()


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

