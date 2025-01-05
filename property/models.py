from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=66)
    image =models.ImageField(upload_to="property/")
    num_bed = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=20000)
    category = models.ForeignKey("Category",related_name='propert_category', on_delete=models.CASCADE)
    place = models.ForeignKey("Place", related_name=("property_place"), on_delete=models.CASCADE)
    num_bathroom = models.IntegerField(default=1)
    cteated_at = models.DateTimeField(default= timezone.now)
    slug = models.SlugField(null = True , blank = True)



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Property, self).save(*args, **kwargs)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("property:property_detail", kwargs={"slug": self.slug})
    
    


class PropertyImage(models.Model):

    property = models.ForeignKey("Property", related_name="property_image", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='propertyimages/')

    def __str__(self):
        return str(self.property)
    
class Place(models.Model):

    name = models.CharField( max_length=500)
    image = models.ImageField(upload_to='places/')


    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


COUNT = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
]

class PropertyBook(models.Model):
    user = models.ForeignKey(User, related_name='book_owner', on_delete=models.CASCADE)
    property = models.ForeignKey('Property', related_name='book_property', on_delete=models.CASCADE)
    date_form = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    guest = models.CharField(max_length=2 , choices=COUNT)
    children = models.CharField(max_length=2 , choices=COUNT)

    def __str__(self):
        return str(self.property)