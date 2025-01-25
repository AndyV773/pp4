from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from crypto_channel.models import Channel, Post


# Create your views here
# Credit for the profile code: Code Institute Boutique Ado project
def profile_account(request):
    """
    Display the user's profile

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
    
    """
    profile_account = get_object_or_404(User, username=username)
    channel_list = Channel.objects.filter(approved=True)
    posts = Post.objects.filter(approved=True)
    profile = get_object_or_404(UserProfile, user=profile_account)

    return render(
        request,
        "profile/profile_detail.html",
        {
            "channel_list": channel_list,
            'profile': profile,
            'profile_account': profile_account,
            'posts': posts,
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
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Profile saved'
            )
            return redirect('profile')
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
