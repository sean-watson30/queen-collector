from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Queen, Category, Photo
from .forms import LipSyncsForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/' # or whatever region you used
BUCKET = ''

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

@login_required
def queens_index(request):
  queens = Queen.objects.all()
  return render(request, 'queens/index.html', { 'queens': queens })

@login_required
def queens_detail(request, queen_id):
  queen = Queen.objects.get(id=queen_id)
  not_walked = Category.objects.exclude(id__in = queen.category.all().values_list('id'))
  lipsyncs_form = LipSyncsForm()
  return render(request, 'queens/detail.html', {
    'queen': queen, 'lipsyncs_form': lipsyncs_form, 'walks': not_walked
  })
  # need to change naming here?


@login_required
def add_lipsync(request, queen_id):
  form = LipSyncsForm(request.POST)
  if form.is_valid():
    new_lipsync = form.save(commit=False)
    new_lipsync.queen_id = queen_id
    new_lipsync.save()
  return redirect('detail', queen_id=queen_id)


# ___________ Many to Many Associations ___________
@login_required
def assoc_category(request, queen_id, category_id):
  Queen.objects.get(id=queen_id).category.add(category_id)
  return redirect('detail', queen_id=queen_id)

@login_required
def assoc_category_delete(request, queen_id, category_id):
  Queen.objects.get(id=queen_id).category.remove(category_id)
  return redirect('detail', queen_id=queen_id)


# ___________ Photo Handling ___________  
@login_required
def add_photo(request, queen_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 =boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, queen_id=queen_id)
      photo.save()
    except Exception as error:
      print('An error occurred uploading file to s3', error)
      return redirect('detail', queen_id=queen_id)
  return redirect('detail', queen_id=queen_id)


# ___________ Sign Up Function ___________
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid information. Please try again.'
  form = UserCreationForm()
  context = { 'form': form, 'error_message': error_message }
  return render(request, 'registration/signup.html', context)  


# ___________ Class Declarations / Queen ___________
class QueenCreate(LoginRequiredMixin, CreateView):
  model = Queen
  # fields = '__all__'
  fields = ['name', 'season', 'description']
  success_url = '/queens/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class QueenUpdate(LoginRequiredMixin, UpdateView):
  model = Queen
  fields = ['season', 'description']
# add 'winner' above?

class QueenDelete(LoginRequiredMixin, DeleteView):
  model = Queen
  success_url = '/queens/'


# ___________ Class Declarations / Category ___________

class CategoryList(LoginRequiredMixin, ListView):
  model = Category
  template_name = 'category/index.html'

class CategoryDetail(LoginRequiredMixin, DetailView):
  model = Category
  template_name = 'category/detail.html'

class CategoryCreate(LoginRequiredMixin, CreateView):
  model = Category
  fields = ['name']
  success_url = '/category/'

class CategoryUpdate(LoginRequiredMixin, UpdateView):
  model = Category
  fields = ['name']

class CategoryDelete(LoginRequiredMixin, DeleteView):
  model = Category
  success_url = '/category/'