from django.urls import path
from .views import Home, convert

app_name = 'temperature'

urlpatterns = [
path('',Home, name='home'),
path('temperature/',convert, name='temperature-conversion'),
]