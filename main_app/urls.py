from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('queens/', views.queens_index, name='index'),
  path('queens/<int:queen_id>', views.queens_detail, name='detail'),
  path('queens/create/', views.QueenCreate.as_view(), name='queens_create'),
  path('queens/<int:pk>/update', views.QueenUpdate.as_view(), name='queens_update'),
  path('queens/<int:pk>/delete', views.QueenDelete.as_view(), name='queens_delete'),
]
