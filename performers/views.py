from django.shortcuts import render
from rest_framework import generics
from performers.models import Performer
from performers.serializers import PerformerSerializer

class PerformerListCreateView(generics.ListCreateAPIView):
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer

class PerformerRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer