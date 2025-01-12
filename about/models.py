from django.db import models

# Create your models here.
class About(models.Model):
    """
    Stores a single about me text.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactRequest(models.Model):
    """
    Stores a single collaboration request message.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=280)
    read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact request from {self.name}"
