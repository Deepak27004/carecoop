# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-06 10:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0005_auto_20170902_1201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photogallery',
            options={'ordering': ['-created'], 'verbose_name': 'PHOTO GALLERY', 'verbose_name_plural': 'PHOTO GALLERIES'},
        ),
    ]