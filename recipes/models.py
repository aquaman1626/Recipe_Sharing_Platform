from django.db import models
from users.models import CustomUser
from django.conf import settings
from ratings.models import Rating

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    ingredients = models.TextField()
    steps = models.TextField()
    cuisine = models.CharField(max_length=100)
    cooking_time = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

def __str__(self):
        return f"{self.user.email} - {self.recipe.title} - {self.score}"