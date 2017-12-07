# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.Album', verbose_name='\u0410\u043b\u044c\u0431\u043e\u043c'),
        ),
    ]