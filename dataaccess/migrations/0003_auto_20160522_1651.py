# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-22 16:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataaccess', '0002_auto_20160522_1029'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserProfile',
        ),
    ]