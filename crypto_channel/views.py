from django.shortcuts import render, get_object_or_404, reverse
from django.utils.text import slugify
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Channel, Post, Comment
from profile.models import UserProfile
from .forms import AddChannelForm, PostForm, CommentForm


# Create your views here.
class ChannelList(generic.ListView):
    """
    View to display a list of channels
    """
    queryset = Channel.objects.filter(approved=True)
    template_name = "crypto_channel/index.html"


def add_channel(request):
    """
    Display add channel form for channel requests

    **Context**
    ``channel_list``
        All approved channels related to :model:`crypto_channel.Channel`
    ``add_channel_form``
        An instance of :form:`crypto_channel.AddChannelForm`

    **Template:**
    :template:`crypto_channel/add_channel.html`
    """
    if request.method == 'POST':
        add_channel_form = AddChannelForm(data=request.POST)
        if add_channel_form.is_valid():
            channel = add_channel_form.save(commit=False)
            channel.name = channel.name.lower()
            channel.slug = slugify(channel.name)
            # checks if channel request already exist
            if Channel.objects.filter(slug=channel.slug).exists():
                messages.add_message(request, messages.ERROR,
                                     'Error requesting channel. '
                                     'Check it does not already exist!')
            else:
                channel.save()
                messages.add_message(
                        request, messages.SUCCESS,
                        'Channel request sent'
                    )
                return HttpResponseRedirect(reverse('add_channel'))
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error requesting channel. '
                                 'Check it does not already exist!')

    channel_list = Channel.objects.filter(approved=True)
    # resets content of form
    add_channel_form = AddChannelForm()

    return render(
            request,
            "crypto_channel/add_channel.html",
            {
                "channel_list": channel_list,
                "add_channel_form": add_channel_form,
            },  # context
        )


def channel_detail(request, slug):
    """
    Display an individual :model:`crypto_channel.Channel`

    **Context**
    ``posts``
        All approved posts related to the channel
    ``post_count``
        A count of approved posts related to the channel
    ``post.liked``
        Returns a True or False instance of a liked post
    ``post.comment_count``
        A count of approved comments related to a post
    ``channel``
        An instance of :model:`crypto_channel.Channel`
    ``channel_list``
        All approved channels related to :model:`crypto_channel.Channel`
    ``post_form``
        An instance of :form:`crypto_channel.PostForm`
    ``post.profile``
        A instance of post author related :model:`profile.UserProfile`

    **Template:**
    :template:`crypto_channel/channel_detail.html`
    """

    channel_list = Channel.objects.filter(approved=True)
    channel = get_object_or_404(channel_list, slug=slug)
    posts = channel.channel_posts.filter(approved=True,
                                         status=1).order_by("-created_on")
    post_count = channel.channel_posts.filter(approved=True,
                                              status=1).count()
    # Credit for post.comment_count: code institute tutoring
    # returns comment count to a post instance
    # https://github.com/Code-Institute-Solutions/
    # Django3blog/blob/master/10_likes/blog/views.py
    liked = False
    for post in posts:
        post.comment_count = post.comments.filter(approved=True).count()
        post.profile = UserProfile.objects.get(user=post.author)
        if post.likes.filter(id=request.user.id).exists():
            post.liked = True

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.channel = channel
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Post sent'
            )
            return HttpResponseRedirect(reverse('channel_detail', args=[slug]))
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error sending post!')

    # resets content of form
    post_form = PostForm()

    return render(
        request,
        "crypto_channel/channel_detail.html",
        {
            "channel_list": channel_list,
            "channel": channel,
            "posts": posts,
            "post_count": post_count,
            "post_form": post_form,
        },  # context
    )


# Credit for PostLike code: code institute
# https://github.com/Code-Institute-Solutions/
# Django3blog/blob/master/10_likes/blog/views.py
class PostLike(View):
    """
    post an individual like to a post related to the user

    **context**
    ``post``
        An instance of :model:`crypto_channel.Post`
    """
    def post(self, request, slug, post_id, *args, **kwargs):
        post = get_object_or_404(Post, id=post_id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('channel_detail', args=[slug]))


def post_detail(request, slug, post_id):
    """
    Display an individual :model:`crypto_channel.Post`

    **Context**
    ``post``
        An instance of :model:`crypto_channel.Post`
    ``comments``
        All approved comments related to the post
    ``comment_count``
        A count of approved comments related to a post
    ``channel``
        An instance of :model:`crypto_channel.Channel`
    ``channel_list``
        All approved channels related to :model:`crypto_channel.Channel`
    ``comment_form``
        An instance of :form:`crypto_channel.CommnetForm`
    ``profile``
        A instance of post author related :model:`profile.UserProfile`
    ``comment.profile``
        A instance of comment author related to:model:`profile.UserProfile`

    **Template:**
    :template:`crypto_channel/post_detail.html`
    """
    channel_list = Channel.objects.filter(approved=True)
    channel = get_object_or_404(Channel, slug=slug)
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.filter(approved=True).order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    profile = UserProfile.objects.get(user=post.author)

    for comment in comments:
        comment.profile = UserProfile.objects.get(user=comment.author)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.channel = channel
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment sent'
            )
            return HttpResponseRedirect(reverse('post_detail',
                                                args=[slug, post_id]))
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error sending comment!')

    # resets content of form
    comment_form = CommentForm()

    return render(
        request,
        "crypto_channel/post_detail.html",
        {
            "channel_list": channel_list,
            "channel": channel,
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "profile": profile,
        },  # context
    )


def post_edit(request, slug, post_id):
    """
    Display an individual post for edit.

    **context**
    ``post``
        An instance of :model:`crypto_channel.Post`
    ``channel``
        An instance of :model:`crypto_channel.Channel`
    ``post_form``
        An instance of :form:`crypto_channel.PostForm`
    """
    if request.method == "POST":

        channel = get_object_or_404(Channel, slug=slug)
        post = get_object_or_404(Post, id=post_id)
        post_form = PostForm(request.POST, request.FILES, instance=post)

        if post_form.is_valid() and post.author == request.user:
            post = post_form.save(commit=False)
            post.channel = channel
            post.save()
            messages.add_message(
                    request, messages.SUCCESS,
                    'Post updated'
                )
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating post!')

    return HttpResponseRedirect(reverse('channel_detail', args=[slug]))


def post_delete(request, slug, post_id):
    """
    Delete an individual post

    **context**
    ``post``
        An instance of :model:`crypto_channel.Post`
    """
    post = get_object_or_404(Post, pk=post_id)

    if post.author == request.user:
        post.delete()
        messages.add_message(
                request, messages.SUCCESS,
                'Post deleted'
            )
    else:
        messages.add_message(request, messages.ERROR,
                             'Error deleting post!')

    return HttpResponseRedirect(reverse('channel_detail', args=[slug]))


def comment_edit(request, slug, post_id, comment_id):
    """
    Display an individual comment for edit.

    **context**
    ``post``
        An instance of :model:`crypto_channel.Post`
    ``comment``
        An instance of :model:`crypto_channel.Comment`
    ``comment_form``
        An instance of :form:`crypto_channel.CommnetForm`
    """
    if request.method == "POST":

        post = get_object_or_404(Post, pk=post_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment updated'
            )
    else:
        messages.add_message(request, messages.ERROR,
                             'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug, post_id]))


def comment_delete(request, slug, post_id, comment_id):
    """
    Delete an individual comment.

    **context**
    ``comment``
        An instance of :model:`crypto_channel.Comment`
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(
                request, messages.SUCCESS,
                'Comment deleted'
            )
    else:
        messages.add_message(request, messages.ERROR,
                             'Error deleting comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug, post_id]))
