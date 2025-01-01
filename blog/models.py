from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User,related_name='post_authror', on_delete=models.CASCADE)
    titel = models.CharField(max_length=500)
    image = models.ImageField(upload_to='post/')
    create_at = models.DateTimeField(default=timezone.now)
    