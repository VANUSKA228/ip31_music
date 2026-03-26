from django.db import models


class Genre(models.Model):
    name_en = models.CharField(max_length=100, verbose_name="Название (EN)")
    name_ru = models.CharField(max_length=100, verbose_name="Название (RU)")
    description = models.TextField(verbose_name="Описание")
    def __str__(self):
        return self.name_ru
    
class Artist(models.Model)
    name = models.CharField(max_length=500, unique=True)
    image = models.ImageField(upload_to='artists/', blank=True, null=True)

    def __str__(self):
        return self.name

class Track(models.Model):
    title = models.CharField(max_length=500,unique=True)
    duration =models.DurationField()
    genres = models.ManyToManyField(Genre)
    artist = models.ForeignKey(Artist, on_delete=models.RESTRICT, null=True)
    def __str__(self):
        return self.title