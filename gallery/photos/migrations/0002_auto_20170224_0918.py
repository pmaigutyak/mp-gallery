# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-24 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u041e\u043f\u0438\u0441'),
        ),
    ]