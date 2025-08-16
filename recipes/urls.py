from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeSearchView

urlpatterns = [
    path('recipes/', RecipeListView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/search/', RecipeSearchView.as_view(), name='recipe-search'),
]