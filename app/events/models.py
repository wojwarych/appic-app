from django.db import models

class Artist(models.Model):

    class MusicGenre(models.TextChoices):
        ROCK = "rock", "Rock"
        POP = "pop", "Pop"
    name = models.CharField(unique=True, max_length=255)
    music_genre = models.CharField(unique=True, max_length=255, choices=MusicGenre.choices)

    def __str__(self):
        return f"{self.name}"



class Event(models.Model):
    name = models.CharField(unique=True, max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()


class Performance(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
