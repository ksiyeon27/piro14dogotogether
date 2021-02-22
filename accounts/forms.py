from django import forms
from .models import Profile
from imagekit.models import ImageSpecField
from django.contrib.auth.hashers import check_password

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['image', 'nickname', 'name', 'email']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input-lg'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-pw'}))