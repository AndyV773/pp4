from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Channel(models.Model):
    """
    Stores a single channel
    """
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    """
    Stores a single crypto post entry related to :model:`auth.User`.
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_posts"
    )
    channel = models.ForeignKey(
        Channel, on_delete=models.CASCADE, related_name="channel_posts"
    )
    content = models.TextField(max_length=280)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Written by {self.author}"
