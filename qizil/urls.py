from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('gold/<str:pk>/', views.gold , name='gold'),
    path('goldform/', views.addgold, name='addgold'),
    path('editgold/<str:pk>/', views.editgold, name='editgold'),
    path('delgold/<str:pk>/', views.delgold, name='delgold'),


]