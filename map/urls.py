from django.urls import path, re_path
from . import views
app_name = 'map'

urlpatterns = [
    path('', views.showmap, name='showmap'),
    path('test/', views.testmap, name='testmap'),
    path('create/', views.register_place,name='register'),
]