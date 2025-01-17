from django.contrib import admin
from .models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the User Profile model
    """
    list_display = ('user', 'phone_number', 'post_code')
    search_fields = ['post_code']
    list_filter = ('post_code',)
