from django.urls import path
from . import views


urlpatterns = [
    path('', views.ChannelList.as_view(), name='home'),
    path('add_channel/', views.add_channel, name='add_channel'),
    # channel url
    path('<slug:slug>/', views.channel_detail, name='channel_detail'),
    # post url
    path('<slug:slug>/<int:post_id>/', views.post_detail, name='post_detail'),
    # post edit and delete urls
    path('<slug:slug>/edit_post/<int:post_id>/', views.post_edit, name='post_edit'),
    path('<slug:slug>/delete_post/<int:post_id>/', views.post_delete, name='post_delete'),
    # comment edit and delete urls
    path('<slug:slug>/<int:post_id>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/<int:post_id>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]
