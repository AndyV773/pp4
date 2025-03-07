from django.contrib import admin
from .models import Channel, Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Channel model
    """
    list_display = ('name', 'rank', 'slug', 'approved', 'created_on')
    search_fields = ['name', 'rank']
    list_filter = ('approved',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Post model, with Summernote integration
    for rich text.
    """
    list_display = ('author', 'channel', 'content',
                    'status', 'approved', 'created_on')
    search_fields = ['author__username', 'channel__name']
    list_filter = ('status', 'created_on', 'approved')
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Comment model.
    """
    list_display = ('author', 'channel', 'post',
                    'comment', 'approved', 'created_on')
    search_fields = ['author__username', 'channel__name']
    list_filter = ('created_on', 'approved')
    summernote_fields = ('comment',)
