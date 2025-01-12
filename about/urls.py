from django.urls import path
from . import views


urlpatterns = [
    path('', views.about_me, name='about'),
    path('contact/', views.contact_me, name='contact'),
]
