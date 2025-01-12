from django.contrib import admin
from .models import About, ContactRequest
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the About model, with Summernote integration
    for rich text.
    """
    list_display = ('title', 'updated_on')
    summernote_fields = ('content',)

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    """
    Admin configuration for the ContactRequest model.
    """
    list_display = ('name', 'message', 'read', 'created_on')
    list_filter = ('read',)
