# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-07 17:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import gallery.videos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('logo', models.ImageField(blank=True, upload_to=gallery.videos.models.get_album_upload_path, verbose_name='\u041b\u043e\u0433\u043e\u0442\u0438\u043f')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='\u041e\u043f\u0438\u0441')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
                'verbose_name': '\u0410\u043b\u044c\u0431\u043e\u043c',
                'verbose_name_plural': '\u0410\u043b\u044c\u0431\u043e\u043c\u0438',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('logo', models.ImageField(blank=True, upload_to=gallery.videos.models.get_video_logo_upload_path, verbose_name='\u041b\u043e\u0433\u043e\u0442\u0438\u043f')),
                ('code', models.CharField(max_length=255, verbose_name='\u041a\u043e\u0434')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='\u041e\u043f\u0438\u0441')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='videos.Album', verbose_name='\u0410\u043b\u044c\u0431\u043e\u043c')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
                'verbose_name': '\u0412\u0456\u0434\u0435\u043e',
                'verbose_name_plural': '\u0412\u0456\u0434\u0435\u043e',
            },
        ),
    ]
