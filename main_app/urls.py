from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('queens/', views.queens_index, name='index'),
  path('queens/<int:queen_id>', views.queens_detail, name='detail'),
  path('queens/create/', views.QueenCreate.as_view(), name='queens_create'),
  path('queens/<int:pk>/update/', views.QueenUpdate.as_view(), name='queens_update'),
  path('queens/<int:pk>/delete/', views.QueenDelete.as_view(), name='queens_delete'),
  path('queens/<int:queen_id>/add_lipsync/', views.add_lipsync, name='add_lipsync'),
  # adding photo url path
  path('queens/<int:queen_id>/add_photo/', views.add_photo, name='add_photo'),
# associated links go here
  path('queens/<int:queen_id>/assoc_category/<int:category_id>/', views.assoc_category, name='assoc_category'),
  path('queens/<int:queen_id>/assoc_category/<int:category_id>/delete/', views.assoc_category_delete, name='assoc_category_delete'),
# associated links go here
  path('category/', views.CategoryList.as_view(), name='category_index'),
  path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category_detail'),
  path('category/create/', views.CategoryCreate.as_view(), name='category_create'),
  path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category_update'),
  path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]
