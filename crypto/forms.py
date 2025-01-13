from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
    Form for submitting a post to a single channel
    """
    class Meta:
        model = Post
        fields = ('content', 'status',)


class CommentForm(forms.ModelForm):
    """
    Form for submitting a comment to a single post
    """
    class Meta:
        model = Comment
        fields = ('comment',)
