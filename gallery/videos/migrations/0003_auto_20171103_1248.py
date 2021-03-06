# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 12:48
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('videos', '0002_auto_20170329_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='video_albums', to='sites.Site', verbose_name='Site'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u0406\u043c\u02bc\u044f'),
        ),
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u0406\u043c\u02bc\u044f'),
        ),
    ]
