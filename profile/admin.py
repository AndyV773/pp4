from django.contrib import admin
from .models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the User Profile model
    """
    list_display = ('user', 'default_phone_number', 'default_postcode')
    search_fields = ['default_postcode']
    list_filter = ('default_postcode',)
