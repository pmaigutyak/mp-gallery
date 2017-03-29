# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-29 08:16
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import gallery.photos.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20170224_0918'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ('order',), 'verbose_name': '\u0410\u043b\u044c\u0431\u043e\u043c', 'verbose_name_plural': '\u0410\u043b\u044c\u0431\u043e\u043c\u0438'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ('order',), 'verbose_name': '\u0424\u043e\u0442\u043e', 'verbose_name_plural': '\u0424\u043e\u0442\u043e'},
        ),
        migrations.RenameField(
            model_name='album',
            old_name='description',
            new_name='short_description',
        ),
        migrations.AddField(
            model_name='album',
            name='full_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=10000, verbose_name='Full description'),
        ),
        migrations.AlterField(
            model_name='album',
            name='logo',
            field=models.ImageField(blank=True, upload_to=gallery.photos.models.get_album_upload_path, verbose_name='\u041b\u043e\u0433\u043e\u0442\u0438\u043f'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=255, verbose_name="\u0406\u043c'\u044f"),
        ),
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='photos.Album', verbose_name='\u0410\u043b\u044c\u0431\u043e\u043c'),
        ),
    ]