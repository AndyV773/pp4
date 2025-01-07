from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Channel(models.Model):
    """
    Stores a single channel
    """
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
