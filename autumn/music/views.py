# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from music.models import Track, Album


def track_list(request):
    tracks = Track.objects.all()
    titles = ' '.join([track.title for track in tracks])
    return HttpResponse(titles)


def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    tracks = Track.objects.filter(album=album)
    track_names = '<br/>'.join([track.title for track in tracks])
    result = '<h1>{album}</h1><div>{track_names}</div>'.format(
        album=album.title, track_names=track_names
    )
    return HttpResponse(result)
