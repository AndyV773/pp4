from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm


# Create your views here.
def profile_detail(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()


    profile_form = UserProfileForm(instance=profile)

    return render(
        request,
        "profile/profile_detail.html",
        {
            'profile_form': profile_form,
            'on_profile_page': True,
        },  # context
    )
