# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-24 11:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataaccess', '0008_auto_20160524_1108'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([]),
        ),
    ]
