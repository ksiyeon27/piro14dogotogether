from django.urls import path
from . import views

app_name = 'calculator'

urlpatterns = [
    path('', views.firstpage, name='firstpage'),
    path('calculate/', views.calculator, name='calculate'),
]