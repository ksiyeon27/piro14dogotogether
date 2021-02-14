from django import forms
from .models import Profile
from imagekit.models import ImageSpecField
from django.contrib.auth.hashers import check_password

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['name','nickname','email','image']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input-lg'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-pw'}))


# 계정 탈퇴 비밀번호 확인 폼
class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
    attrs={'class': 'form-control',}))

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password
        
        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')