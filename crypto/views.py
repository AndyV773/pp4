from django.shortcuts import render, get_object_or_404, reverse
from django.utils.text import slugify
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Channel, Post, Comment
from .forms import AddChannelForm, PostForm, CommentForm

# Create your views here.
class ChannelList(generic.ListView):
    """
    View to display a list of channels
    """
    # all().order_by("rank")
    queryset = Channel.objects.filter(approved=True)
    template_name = "crypto/index.html"


def add_channel(request):
    """
    Allows user to make a contact requests
    **Context**

    **Template:**
    :template:`crypto/add_channel.html`
    """
    if request.method == 'POST':
        add_channel_form = AddChannelForm(data=request.POST)
        if add_channel_form.is_valid():
            channel = add_channel_form.save(commit=False)
            channel.slug = slugify(channel.name)
            channel.save()
            messages.add_message(
                    request, messages.SUCCESS,
                    'Channel request sent'
                )
        else:
            messages.add_message(request, messages.ERROR,
                                    'Error requesting channel!')

    channel_list = Channel.objects.filter(approved=True)
    add_channel_form = AddChannelForm()        

    return render(
            request,
            "crypto/add_channel.html",
            {
                "channel_list": channel_list,
                "add_channel_form": add_channel_form,
            },  # context
        )



def channel_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    :template:`crypto/channel_detail.html`
    """

    channel_list = Channel.objects.filter(approved=True)
    channel = get_object_or_404(channel_list, slug=slug)
    posts = channel.channel_posts.filter(status=1).order_by("-created_on")
    post_count = channel.channel_posts.filter(approved=True, status=1).count()
    
    comment_list = Comment.objects.all()
    comment_count = comment_list.filter(approved=True).count()

    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.channel = channel
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Post sent'
            )
        else:
            messages.add_message(request, messages.ERROR,
                                    'Error sending post!')

    post_form = PostForm()  # resets content of form

    return render(
        request,
        "crypto/channel_detail.html",
        {
            "channel_list": channel_list,
            "channel": channel,
            "posts": posts,
            "post_count": post_count,
            "comment_count": comment_count,
            "post_form": post_form,
        },  # context
    )


def post_detail(request, slug, post_id):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    :template:`crypto/post_detail.html`
    """
    channel_list = Channel.objects.filter(approved=True)
    channel = get_object_or_404(Channel, slug=slug)
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

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
        else:
            messages.add_message(request, messages.ERROR,
                                    'Error sending comment!')

    comment_form = CommentForm()  # resets content of form

    return render(
        request,
        "crypto/post_detail.html",
        {
            "channel_list": channel_list,
            "channel": channel,
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },  # context
    )


def post_edit(request, slug, post_id):
    """
    Display an individual comment for edit.

    **context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        A single comment related to the post.
    ``coment_form``
        An instance of :form:`blog.CommentForm`.
    """
    if request.method == "POST":

        channel_list = Channel.objects.filter(approved=True)
        channel = get_object_or_404(Channel, slug=slug)
        post = Post.objects.filter(status=1)
        post = get_object_or_404(post, id=post_id)
        post_form = PostForm(data=request.POST, instance=post)

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
    Delete an individual comment.

    **context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        A single comment related to the post.
    """
    channel_list = Channel.objects.filter(approved=True)
    channel = get_object_or_404(channel_list, slug=slug)
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
        An instance of :model:`blog.Post`.
    ``comments``
        A single comment related to the post.
    ``coment_form``
        An instance of :form:`blog.CommentForm`.
    """
    if request.method == "POST":

        channel = get_object_or_404(Channel, slug=slug)
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

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        A single comment related to the post.
    """

    channel = get_object_or_404(Channel, slug=slug)
    post = get_object_or_404(Post, pk=post_id)
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
