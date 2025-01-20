from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User,related_name='post_authror', on_delete=models.CASCADE)
    titel = models.CharField(max_length=500)
    image = models.ImageField(upload_to='post/')
    create_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, blank=True, null=True)  # أضف هذا الحقل


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titel)  # استخدم self.titel الصحيح
        super(Post, self).save(*args, **kwargs)  # استخدم self بدلًا من salf

    def __str__(self):
        return self.titel  # اسم الحقل الصحيح


    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
    
    