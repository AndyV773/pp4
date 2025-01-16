from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from crypto.models import Channel


# Create your views here
def profile_detail(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    channel_list = Channel.objects.filter(approved=True)

    return render(
        request,
        "profile/profile_detail.html",
        {
            "channel_list": channel_list,
            'profile': profile,
            'on_profile_page': True,
        },  # context
    )


def edit_profile(request):
    """ Display the user's profile. """
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
            'on_profile_page': True,
        },  # context
    )
