from django.urls import path
from . import views


urlpatterns = [
    path('', views.my_channels, name='home'),
]