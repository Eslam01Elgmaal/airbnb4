from django.urls import path
from .views import PropertyList , PropertyDetail

app_name = 'property'

urlpatterns = [
    path('' , PropertyList.as_view()),
    path('' , PropertyDetail.as_view())
]