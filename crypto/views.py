from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from .models import Channel, Post

# Create your views here.
class ChannelList(generic.ListView):
    """
    View to display a list of channels
    """
    # all().order_by("rank")
    queryset = Channel.objects.all()
    template_name = "crypto/index.html"


def channel_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    :template:`crypto/channel_detail.html`
    """

    queryset = Channel.objects.all()
    channel = get_object_or_404(queryset, slug=slug)
    posts = channel.channel_posts.all().order_by("-created_on")
    post_count = channel.channel_posts.filter(approved=True).count()


    return render(
        request,
        "crypto/channel_detail.html",
        {
            "channel_list": queryset,
            "channel": channel,
            "posts": posts,
            "post_count": post_count,
        },  # context
    )