from django.urls import path, re_path
from . import views
app_name = 'map'

urlpatterns = [
    path('', views.showmap, name='showmap'),
    path('search/<str:searchword>/', views.search, name='searchmap'),
    path('test/', views.testmap, name='testmap'),
    path('ajax/', views.addplace, name='ajax'),
    path('ajax/delete', views.deleteplace,name='delete'),
    path('search/<str:searchword>/ajax/', views.addplacebysearch, name='searchajax'),
    path('search/<str:searchword>/ajax/delete', views.deleteplacebysearch, name='searchdelete'),
]