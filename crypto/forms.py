from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
    Form for submitting single post to a channel
    """
    class Meta:
        model = Post
        fields = ('content', 'status',)
