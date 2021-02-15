from django.urls import path, re_path
from . import views
app_name = 'map'

urlpatterns = [
    path('', views.showmap, name='showmap'),
    path('test/', views.testmap, name='testmap'),
    path('ajax/', views.addplace, name='ajax'),
    path('ajax/delete',views.deleteplace,name='delete'),
]