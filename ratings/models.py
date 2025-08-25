from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import CustomUser
from django.utils import timezone



# Create your models here.

class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.IntegerField(default=1)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating from 1 (worst) to 5 (best)"
    )
    timestamp = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"{self.user} - {self.recipe} ({self.score})"