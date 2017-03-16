# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-19 15:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import gallery.photos.models


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
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('logo', models.ImageField(blank=True, upload_to=gallery.photos.models.get_album_upload_path, verbose_name='Logo')),
                ('description', models.CharField(max_length=255, verbose_name='\u041e\u043f\u0438\u0441')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('file', models.ImageField(upload_to=gallery.photos.models.get_photo_upload_path, verbose_name='\u0424\u0430\u0439\u043b')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Album', verbose_name='Album')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
            },
        ),
    ]