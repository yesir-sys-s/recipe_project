from django.urls import path
from .views import (
    HomeView,
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    RecipeUpdateView,
    RecipeDeleteView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('recipes/', RecipeListView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/new/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipes/<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipes/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
]