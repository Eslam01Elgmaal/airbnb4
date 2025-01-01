from django.contrib import admin
from .models import Property , PropertyImage , Place , Category , PropertyBook

# Register your models here.
admin.site.register(Property)
admin.site.register(PropertyImage)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(PropertyBook)