from music.views import track_list, album_detail, album_detail_data, track_add
from django.conf.urls import url

urlpatterns = [
    url(r'^track/list/$', track_list, name='track_list'),
    url(r'^track/add/$', track_add, name='track_add'),
    url(
        r'^album/(?P<album_id>\d+)/$',
        album_detail, name='album_detail'
    ),
    url(
        r'^album/(?P<album_id>\d+)/data/$',
        album_detail_data, name='album_detail_data'
    ),
]
