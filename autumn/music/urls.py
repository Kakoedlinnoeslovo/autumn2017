from music.views import track_list, album_detail
from django.conf.urls import url

urlpatterns = [
    url(r'^track/list/$', track_list, name='track_list'),
    url(
        r'^album/(?P<album_id>\d+)/$',
        album_detail, name='album_detail'
    ),
]
