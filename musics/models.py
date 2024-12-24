from django.db import models
from performers.models import Performer
from genres.models import Genre

class Music(models.Model):
    title = models.CharField(max_length=300)
    performers = models.ManyToManyField(Performer, blank=True, related_name='musics')
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='musics')
    album = models.CharField(max_length=300, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title