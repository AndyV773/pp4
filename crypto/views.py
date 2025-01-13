from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponse
from .models import Channel, Post, Comment

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

    channel_list = Channel.objects.all()
    channel = get_object_or_404(channel_list, slug=slug)
    posts = channel.channel_posts.filter(status=1).order_by("-created_on")
    post_count = channel.channel_posts.filter(approved=True, status=1).count()
    comment = Comment.objects.all()
    comment_count = comment.filter(approved=True).count()


    return render(
        request,
        "crypto/channel_detail.html",
        {
            "channel_list": channel_list,
            "channel": channel,
            "posts": posts,
            "post_count": post_count,
            "comment_count": comment_count,
        },  # context
    )


def post_detail(request, slug, post_id):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    :template:`crypto/post_detail.html`
    """
    channel_list = Channel.objects.all()
    channel = get_object_or_404(Channel, slug=slug)
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    return render(
        request,
        "crypto/post_detail.html",
        {
            "channel_list": channel_list,
            "channel": channel,
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
        },  # context
    )
