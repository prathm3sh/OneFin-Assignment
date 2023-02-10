from django.db import models
from django.contrib.auth.models import User
import uuid


class Genre(models.Model):
  title = models.CharField(max_length=200)

  def __str__(self):
    return self.title


class Movie(models.Model):
  uuid = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
  title = models.CharField(max_length=200)
  description = models.CharField(max_length=500)
  genres = models.ManyToManyField(Genre)

  def __str__(self):
    return self.title


class Collection(models.Model):
  uuid = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
  title = models.CharField(max_length=200)
  description = models.CharField(max_length=500)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  movies = models.ManyToManyField(Movie)

  def __str__(self):
    return str(self.uuid) + ' - ' + self.user.username



