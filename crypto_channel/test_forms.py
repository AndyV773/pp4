from django.test import TestCase
from .forms import AddChannelForm, PostForm, CommentForm
from .models import Channel


# Create your tests here.
class TestAddChannelForm(TestCase):
    """
    Testing AddChannelForm class
    """
    def setUp(self):
        Channel.objects.create(name='koinos')

    def test_form_is_valid(self):
        add_channel_form = AddChannelForm({'name': 'new channel'})
        self.assertTrue(add_channel_form.is_valid(),
                        msg='add channel form is invalid')

    def test_form_exists(self):
        add_channel_form = AddChannelForm({'name': 'koinos'})
        self.assertFalse(add_channel_form.is_valid(),
                         msg="existing channel form is valid")

    def test_blank_form_is_invalid(self):
        add_channel_form = AddChannelForm({'name': ''})
        self.assertFalse(add_channel_form.is_valid(),
                         msg="blank channel form is valid")


class TestCommentForm(TestCase):
    """
    Testing CommentForm class
    """
    def test_form_is_valid(self):
        comment_form = CommentForm({'comment': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(),
                        msg='comment form is invalid')

    def test_blank_form_is_invalid(self):
        comment_form = CommentForm({'comment': ''})
        self.assertFalse(comment_form.is_valid(),
                         msg="blank comment form is valid")
