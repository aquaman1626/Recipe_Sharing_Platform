from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Recipe
from .serializers import RecipeSerializer

# Create your views here.

class RecipeListView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

class RecipeSearchView(generics.ListAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        cuisine = self.request.query_params.get('cuisine', '')
        cooking_time = self.request.query_params.get('cooking_time', 0)

        queryset = Recipe.objects.filter(
            Q(title__icontains=query) |
            Q(ingredients__icontains=query) |
            Q(cuisine__icontains=cuisine) |
            Q(cooking_time__lte=cooking_time)
        )
        return queryset
