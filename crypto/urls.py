from django.urls import path
from . import views


urlpatterns = [
    path('', views.ChannelList.as_view(), name='home'),
    path('<slug:slug>/', views.channel_detail, name='channel_detail'),
]