# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifyme', '0021_auto_20170430_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hasil',
            name='judul',
        ),
        migrations.AddField(
            model_name='buku',
            name='hasil_klasifikasi',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Hasil',
        ),
    ]
