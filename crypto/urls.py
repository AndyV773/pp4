from django.urls import path
from . import views


urlpatterns = [
    path('', views.ChannelList.as_view(), name='home'),
    path('<slug:slug>/', views.channel_detail, name='channel_detail'),
    path('<slug:slug>/edit_post/<int:post_id>',
         views.post_edit, name='post_edit'),
    path('<slug:slug>/delete_post/<int:post_id>',
         views.post_delete, name='post_delete'),
    path('<slug:slug>/<int:post_id>/', views.post_detail, name='post_detail'),
]
