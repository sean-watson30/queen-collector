from django.shortcuts import render
from django.http import HttpResponse
from .models import Queen

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# class Queen:
#   def __init__(self, name, season, description, winner):
#     self.name = name
#     self.season = season
#     self.description = description
#     self.winner = winner

# queens = [
#   Queen('Trixie Mattel', '7 and All Stars 3', 'known for subtlety in her beat', True),
#   Queen('Bianca del Rio', '6', 'killer clown witha  rolodex of hate', True),
#   Queen('Bendela Creme', '6 and All Stars 3', 'terminaly optimistic', False)
# ]

def queens_index(request):
  queens = Queen.objects.all()
  return render(request, 'queens/index.html', { 'queens': queens })