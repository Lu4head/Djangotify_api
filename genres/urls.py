from django.urls import path
from genres.views import GenreListCreateView, GenreDetailView

urlpatterns = [
    path('genres/', GenreListCreateView.as_view(), name='genre-list-create-view'),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genre-detail-view'),
]