# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-01 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=40, null=True, verbose_name='Title')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images%Y/%m/%d', verbose_name='Images')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('details', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('venues', models.CharField(blank=True, max_length=40, null=True, verbose_name='venues')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'ANNOUCEMENT',
                'verbose_name_plural': 'ANNOUNCEMENTS',
            },
        ),
    ]