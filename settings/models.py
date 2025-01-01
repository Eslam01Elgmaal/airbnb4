from django.db import models

# Create your models here.

class Settings(models.Model):
    site_name = models.CharField(max_length=50)
    logo = models.TextField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    address = models.CharField( max_length=500)
    description = models.TextField(max_length=300)
    fc_link = models.URLField(max_length=200)  
    x_link = models.URLField(max_length=200)  
    inst_link = models.URLField(max_length=200)  
    linkedin_link = models.URLField(max_length=200)     

    def __str__(self):
        return self.site_name 
    