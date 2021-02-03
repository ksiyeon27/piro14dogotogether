from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from . import views

app_name='accounts'

urlpatterns = [
    # 이름 수정 필요
    path('', views.base, name='base'),
    path('signup/', views.signup, name='signup'), 
    # django.conf.global_settings에서 login redirect url을 '/accounts/'로 설정
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('profile/delete', views.user_delete, name='user_delete'),

    

]
