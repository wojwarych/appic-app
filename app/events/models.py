from django.db import models

class Artist(models.Model):

    class MuscGenre(models.TextChoices):
        ROCK = "rock", "Rock"
        POP = "pop", "Pop"
    name = models.CharField(unique=True, max_length=255)
    music_genre = models.CharField(unique=True, max_length=255)



class Event(models.Model):
    name = models.CharField(unique=True, max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()


class Performance(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
