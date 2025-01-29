from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from crypto_channel.models import Channel, Post, Comment


# Create your views here
# Credit for the profile code: Code Institute Boutique Ado project
def profile_account(request):
    """
    Display the user's profile account

    **Context**
    ``channel_list``
        All approved channels related to :model:`crypto_channel.Channel`
    ``profile``
        An instance of :model:`profile.UserProfile`

    **Template:**
    :template:`profile/profile_account.html`
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    channel_list = Channel.objects.filter(approved=True)

    return render(
        request,
        "profile/profile_account.html",
        {
            "channel_list": channel_list,
            'profile': profile,
        },  # context
    )


def profile_detail(request, username):
    """
    Display the user's profile detail

    **Context**
    ``channel_list``
        All approved channels related to :model:`crypto_channel.Channel`
    ``posts``
        All approved posts related to :model:`crypto_channel.Post`
    ``post_count``
        A count of approved posts related to the author
    ``profile_detail``
        An instance of :model:`User`
    ``profile``
        An instance of :model:`profile.UserProfile`

    **Template:**
    :template:`profile/profile_detail.html`
    """
    profile_detail = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=profile_detail)
    channel_list = Channel.objects.filter(approved=True)
    posts = Post.objects.filter(approved=True)
    post_count = profile_detail.author_posts.filter(approved=True).count()

    # https://github.com/Code-Institute-Solutions/
    # Django3blog/blob/master/10_likes/blog/views.py
    liked = False
    for post in posts:
        post.comment_count = post.comments.filter(approved=True).count()
        if post.likes.filter(id=request.user.id).exists():
            post.liked = True

    return render(
        request,
        "profile/profile_detail.html",
        {
            "channel_list": channel_list,
            'profile': profile,
            'profile_detail': profile_detail,
            'posts': posts,
            'post_count': post_count,
        },  # context
    )


def edit_profile(request):
    """
    Display pre filled user profile form
    to edit user profile

    **Context**
    ``channel_list``
        All approved channels related to :model:`crypto_channel.Channel`
    ``profile_form``
        An instance of :form:`profile.UserProfileForm`

    **Template:**
    :template:`profile/edit_profile.html`
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Profile saved'
            )
            return redirect('profile_account')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating profile!')

    channel_list = Channel.objects.filter(approved=True)
    profile_form = UserProfileForm(instance=profile)

    return render(
        request,
        "profile/edit_profile.html",
        {
            "channel_list": channel_list,
            'profile_form': profile_form,
        },  # context
    )


def delete_user(request, user_id):
    """
    Delete an individual user

    **context**
    ``user``
        An instance of :model:`django.contrib.auth.User`
    """
    user = get_object_or_404(User, id=user_id)
    if request.user == user:
        user.delete()
        return redirect('/')
