from django import forms
from .models import UserProfile


# user profile form
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
