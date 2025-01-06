from django.contrib import admin
from .models import Channel
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
