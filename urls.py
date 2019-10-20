from django.urls import path

from . import views

urlpatterns = [
    path('', views.FrontPage, name='FrontPage'),
    path('tags', views.TagList, name='TagList'),
    path('clips', views.ClipList, name='ClipList'),
    path('playlist/<str:tag_title>', views.Playlist, name='Playlist'),
    path('subscribe', views.Subscribe, name='Subscribe'),
    path('upload', views.UploadSon, name='UploadSon'),
    path('soundcloud_iframe/<str:soundcloud_id>', views.SoundcloudIframe),
    path('youtube_iframe/<str:youtube_id>', views.YoutubeIframe),
    path('vimeo_iframe/<str:vimeo_id>', views.VimeoIframe),
]