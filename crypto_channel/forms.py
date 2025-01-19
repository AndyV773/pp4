from django import forms
from .models import Channel, Post, Comment


class AddChannelForm(forms.ModelForm):
    """
    Form for submitting a single channel
    """
    class Meta:
        model = Channel
        fields = ('name',)


class PostForm(forms.ModelForm):
    """
    Form for submitting a post to a single channel
    """
    class Meta:
        model = Post
        fields = ('content', 'featured_image',)


class CommentForm(forms.ModelForm):
    """
    Form for submitting a comment to a single post
    """
    class Meta:
        model = Comment
        fields = ('comment',)
