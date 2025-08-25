from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Rating
from .serializers import RatingSerializer

# Create your views here.

class RatingListView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

class RatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

def rate_recipe(request, recipe_id):
    if request.method == "POST":
        rating = request.POST.get("rating")
        if rating:
            Rating.objects.create(
                recipe_id=recipe_id,
                user=request.user,
                rating=int(rating)
            )
            return redirect("recipe-detail", pk=recipe_id)
    return render(request, "ratings/rating_form.html")