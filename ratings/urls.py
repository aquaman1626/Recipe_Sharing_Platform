from django.urls import path,include
from . import views
from ratings.views import RatingListView, RatingDetailView

urlpatterns = [
    #path('recipes/', RecipeListView.as_view(), name='recipe-list'),
    #path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    #path('recipes/search/', RecipeSearchView.as_view(), name='recipe-search'),
    path('ratings/', RatingListView.as_view(), name='rating-list'),
    path("rate/<int:recipe_id>/", views.rate_recipe, name="rate-recipe"),
    path('ratings/<int:pk>/', RatingDetailView.as_view(), name='rating-detail'),
]