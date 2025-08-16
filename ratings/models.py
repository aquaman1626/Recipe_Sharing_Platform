from django.db import models
from users.models import CustomUser
from recipes.models import Recipe

# Create your models here.

class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
