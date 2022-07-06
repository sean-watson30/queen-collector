from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('queens/', views.queens_index, name='index'),
  path('queens/<int:queen_id>', views.queens_detail, name='detail')
]
