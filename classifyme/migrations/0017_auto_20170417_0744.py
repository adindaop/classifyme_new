# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifyme', '0016_auto_20170417_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingsetneg',
            name='nama',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='trainingsetpos',
            name='nama',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
