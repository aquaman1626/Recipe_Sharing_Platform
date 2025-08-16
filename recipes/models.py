from django.db import models
from users.models import CustomUser

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    steps = models.TextField()
    cuisine = models.CharField(max_length=100)
    cooking_time = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)