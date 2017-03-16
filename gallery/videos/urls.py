
from django.conf.urls import url

from gallery.videos import views


urlpatterns = [

    url(r'^$', views.album_list, name='album-list'),

    url(r'^(?P<album_slug>\w+)_(?P<album_pk>\d+)/$', views.video_list,
        name='video-list'),

    url(r'^(?P<album_slug>\w+)_(?P<album_pk>\d+)/'
        r'(?P<video_slug>\w+)_(?P<video_pk>\d+)/$', views.video_info,
        name='video-info'),

]
