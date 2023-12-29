from django.db import models
from musician_app.models import MusicianInfo

# Create your models here.
class AlbumInfo(models.Model):
    album_name = models.CharField(max_length=50)
    release_date = models.DateField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    musician = models.ForeignKey(MusicianInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name