from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Queen, Category
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .forms import LipSyncsForm

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

def queens_detail(request, queen_id):
  queen = Queen.objects.get(id=queen_id)
  lipsyncs_form = LipSyncsForm()
  return render(request, 'queens/detail.html', {
    'queen': queen, 'lipsyncs_form': lipsyncs_form
  })

def add_lipsync(request, queen_id):
  # create the ModelForm using the data in request.POST
  form = LipSyncsForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_lipsync = form.save(commit=False)
    new_lipsync.queen_id = queen_id
    new_lipsync.save()
  return redirect('detail', queen_id=queen_id)
  # return render(request, 'queens/detail.html', { 'queen': queen })

def assoc_category(request, queen_id, category_id):
  Queen.objects.get(id=queen_id).category.add(category_id)
  return redirect('detail', queen_id=queen_id)

def assoc_category_delete(request, queen_id, category_id):
  Queen.objects.get(id=queen_id).category.remove(category_id)
  return redirect('detail', queen_id=queen_id)
  

class QueenCreate(CreateView):
  model = Queen
  fields = '__all__'
  success_url = '/queens'

class QueenUpdate(UpdateView):
  model = Queen
  fields = ['season', 'description']
# add 'winner' above?

class QueenDelete(DeleteView):
  model = Queen
  success_url = '/queens/'

class CategoryList(ListView):
  model = Category
  template_name = 'category/index.html'

class CategoryDetail(DetailView):
  model = Category
  template_name = 'category/detail.html'

class CategoryCreate(CreateView):
  model = Category
  fields = ['name']

class CategoryUpdate(UpdateView):
  model = Category
  fields = ['name']

class CategoryDelete(DeleteView):
  model = Category
  aucess_url = '/category/'