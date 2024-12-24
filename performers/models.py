from django.db import models
from genres.models import Genre

NATIONALITY_CHOICES = (
    ('br', 'Brasileiro'),
    ('us', 'Americano'),
    ('uk', 'Britânico'),
    ('fr', 'Francês'),
    ('it', 'Italiano'),
    ('jp', 'Japonês'),
    ('cn', 'Chinês'),
    ('ru', 'Russo'),
    ('de', 'Alemão'),
    ('es', 'Espanhol'),
    ('ar', 'Argentino'),
    ('mx', 'Mexicano'),
    ('co', 'Colombiano'),
    ('pe', 'Peruano'),
    ('cl', 'Chileno'),
    ('ve', 'Venezuelano'),
    ('ec', 'Equatoriano'),
    ('bo', 'Boliviano'),
    ('py', 'Paraguaio'),
    ('uy', 'Uruguai'),
    ('other', 'Outro')
)

class Performer(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    genre = models.ManyToManyField('genres.Genre')
    image = models.ImageField(upload_to='performers/', blank=True, null=True)
    nationality = models.CharField(max_length=100, choices= NATIONALITY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name