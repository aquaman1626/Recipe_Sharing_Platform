from rest_framework import serializers
from .models import Recipe
from .models import Rating

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'ingredients', 'steps', 'cuisine', 'cooking_time', 'user']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'