from rest_framework import generics
from musics.models import Music
from musics.serializers import MusicSerializer

class MusicListCreateView(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class MusicRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer