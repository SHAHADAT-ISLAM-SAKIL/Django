from django.db import models
# from album_app.models import AlbumInfo

# Create your models here.
class MusicianInfo(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=12)
    Instrument_type = models.CharField(max_length=50)
    # album = models.ManyToManyField(AlbumInfo)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
  