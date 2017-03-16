
from django.conf.urls import url

from gallery.photos import views


urlpatterns = [

    url(r'^$', views.album_list, name='album-list'),

    url(r'^(?P<album_slug>\w+)_(?P<album_pk>\d+)/$', views.photo_list,
        name='photo-list'),

]
