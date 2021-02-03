from django.db import models
from django.conf import settings
# thumbnail import
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# creat profile simultaneously
from django.db.models.signals import post_save


class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    nickname=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    image=models.ImageField(upload_to="accounts")
    image_thumbnail = ImageSpecField(source = 'image', processors = [ResizeToFill(60, 60)])

def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        Profile.objects.create(user=user)

# User 회원 가입 시 Profile 생성하기
post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)
