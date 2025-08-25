from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'recipe', 'rating', 'stars', 'created_at' 'timestamp']
    
    def get_stars(self, obj):
        return "★" * obj.rating + "☆" * (5 - obj.rating)
