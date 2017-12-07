# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from music.models import Track, Album
from music.forms import TrackForm


def track_list(request):
    tracks = Track.objects.all()
    titles = ' '.join([track.title for track in tracks])
    return HttpResponse(titles)


def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    tracks = Track.objects.filter(album=album)
    return render(request, 'album_detail.html', {'tracks': tracks, 'album': album })


def album_detail_data(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    tracks = Track.objects.filter(album=album)
    track_data = [{'id': t.id, 'title': t.title} for t in tracks]
    return JsonResponse({
        'tracks': track_data,
        'album': {'id': album.id, 'title': album.title},
    })


def track_add(request):
    if request.method == 'POST':
        form = TrackForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'ok'})
    else:
        form = TrackForm()
    
    return render(request, 'track_add.html', {'form': form})
