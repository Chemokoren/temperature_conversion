from django.urls import path
from .views import convert

app_name = 'temperature'

urlpatterns = [
path('temperature/',convert, name='temperature-conversion'),
]