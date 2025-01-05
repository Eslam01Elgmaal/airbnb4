from django.contrib import admin
from .models import Property , PropertyImage , Place , Category , PropertyBook
from django_summernote.admin import SummernoteModelAdmin

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

# Register your models here.
admin.site.register(Property, SomeModelAdmin)
admin.site.register(PropertyImage)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(PropertyBook)