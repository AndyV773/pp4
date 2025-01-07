from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Channel

# Create your views here.
class ChannelList(generic.ListView):
    """
    View to display a list of channels
    """
    # all().order_by("rank")
    queryset = Channel.objects.all()
    template_name = "crypto/index.html"


def my_channel(request):
    return HttpResponse("Hello World!")

