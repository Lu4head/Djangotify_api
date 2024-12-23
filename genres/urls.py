from django.urls import path
from genres.views import GenreListCreateView, GenreDetailView

urlpatterns = [
    path('genres/', GenreListCreateView.as_view(), name='genre'),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genre'),
]