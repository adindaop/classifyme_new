# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifyme', '0009_auto_20170404_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='ulasan_testing',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d/'),
        ),
    ]