from django.contrib import admin
from .models import Channel, Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Channel model
    """
    list_display = ('name', 'slug', 'created_on')
    search_fields = ['name', 'created_on']
    list_filter = ('name', 'created_on')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Post model, with Summernote integration
    for rich text.
    """
    list_display = ('title', 'author', 'slug', 'status', 'approved', 'created_on')
    search_fields = ['author', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
