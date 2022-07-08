from django.db import models
from django.forms import BooleanField
from django.urls import reverse

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=100)
  def __str__(self):
    return f'{self.name}'
  def get_absolute_url(self):
    return reverse('category_detail', kwargs={ 'pk': self.id })

class Queen(models.Model):
  name = models.CharField(max_length=100)
  season = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  winner = BooleanField()
  category = models.ManyToManyField(Category)
  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return reverse('detail', kwargs={ 'queen_id': self.id })

class LipSyncs(models.Model):
  season = models.CharField(max_length=50)
  episode = models.CharField(max_length=50)
  song = models.CharField(max_length=100)
  vs = models.CharField(max_length=100)
  queen = models.ForeignKey(Queen, on_delete=models.CASCADE)
  def __str__(self):
    return f"She lip synced for her life to: {self.song}"

class Photo(models.Model):
  url = models.CharField(max_length=200)
  queen = models.ForeignKey(Queen, on_delete=models.CASCADE)
  def __str__(self):
    return f"Photo for queen_id: {self.queen_id} @ this url: {self.url}"