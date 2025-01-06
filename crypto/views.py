from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Channel

# Create your views here.
def my_channel(request):
    return HttpResponse("Hello World!")

