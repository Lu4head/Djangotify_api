from django.urls import path
from musics.views import MusicListCreateView, MusicRetrieveDeleteUpdateView

urlpatterns = [
    path('musics/', MusicListCreateView.as_view(), name='musics-list-create-view'),
    path('musics/<int:pk>/', MusicRetrieveDeleteUpdateView.as_view(), name='music-detail-view') 
]