# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from music.models import Album, Artist, Track
from django.contrib.contenttypes.models import ContentType

admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Track)
admin.site.register(ContentType)
