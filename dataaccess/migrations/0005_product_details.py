# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-23 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataaccess', '0004_auto_20160523_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='details',
            field=models.TextField(default='details'),
            preserve_default=False,
        ),
    ]