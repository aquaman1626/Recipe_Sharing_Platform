from django.urls import path, include
from . import views
from .views import RecipeListView, RecipeDetailView, RecipeSearchView
from rest_framework.routers import DefaultRouter
from .views import RatingViewSet

router = DefaultRouter()
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('recipes/', RecipeListView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/search/', RecipeSearchView.as_view(), name='recipe-search'),
    path("", views.recipe_list, name="recipe-list"),
    path("<int:pk>/", views.recipe_detail, name="recipe-detail"),
    path('', include(router.urls)),
]