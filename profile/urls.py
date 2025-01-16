from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile_detail, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
