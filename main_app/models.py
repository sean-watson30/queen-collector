from django.db import models
from django.forms import BooleanField

# Create your models here.
class Queen(models.Model):
  name = models.CharField(max_length=100)
  season = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  winner = BooleanField()
  def __str__(self):
    return self.name