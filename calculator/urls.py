from django.urls import path
from blog import views

app_name = 'calculator'

urlpatterns = [
    path('', views.calculator, name='calculator'),
]