from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=50)  # TODO validators
    email = models.EmailField(max_length=254)
    age = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)


class Album(models.Model):
    CHOICE_GENRE = (
        ('pop', 'Pop music'),
        ('jazz', 'Jazz music'),
        ('rnb', 'R&B music'),
        ('rock', 'Rock music'),
        ('country', 'Country music'),
        ('dance', 'Dance music'),
        ('hiphop', 'Hip Hop music'),
        ('other', 'Other'),
    )
    album_name = models.CharField(max_length=30, unique=True)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=30, choices=CHOICE_GENRE)
    description = models.TextField(max_length=300, blank=True, null=True)
    image_url = models.URLField(max_length=300, null=False, blank=False)
    price = models.FloatField(validators=[MinValueValidator(0)], null=False, blank=False)