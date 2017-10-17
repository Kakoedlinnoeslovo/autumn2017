# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Track(models.Model):
    title = models.CharField(verbose_name='Название', max_length=256)
    duration = models.IntegerField(verbose_name='Длительность')
    release_date = models.DateField(verbose_name='Дата выпуска')
    artists = models.ManyToManyField(to='Artist', verbose_name='Исполнители')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Композиция'
        verbose_name_plural = 'Композиции'


class Artist(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=256)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Album(models.Model):
    title = models.CharField(verbose_name='Название', max_length=256)
    artist = models.ForeignKey(to=Artist, verbose_name='Основной исполнитель')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
