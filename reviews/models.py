from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from musics.models import Music

class Review(models.Model):
    music = models.ForeignKey(Music, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators= [
            MinValueValidator(0, 'Avaliação não pode ser inferior a 0 estrelas.'),
            MaxValueValidator(5, 'Avaliação não pode ser superior a 5 estrelas.'),
        ] 
    )
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.music}-review"