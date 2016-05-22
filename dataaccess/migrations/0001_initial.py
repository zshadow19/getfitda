# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-22 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=128)),
                ('picture', models.ImageField(blank=True, upload_to='ppic')),
                ('code', models.CharField(max_length=20)),
                ('verified', models.IntegerField(default='0')),
            ],
        ),
    ]