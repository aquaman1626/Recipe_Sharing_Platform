from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rest_framework import viewsets
from .models import Rating
from .serializers import RatingSerializer
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

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

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


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipes/recipe_list.html", {"recipes": recipes})
    
@api_view(['GET'])
def recipe_list(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    serializer = RecipeSerializer(recipe)
    return Response(serializer.data)