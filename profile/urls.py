from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile_account, name='profile_account'),
    path('<username>/', views.profile_detail, name='profile_detail'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
