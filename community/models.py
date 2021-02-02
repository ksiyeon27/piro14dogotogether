from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    likes = models.ManyToManyField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BinaryField(default=False)

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

# Create your models here.
