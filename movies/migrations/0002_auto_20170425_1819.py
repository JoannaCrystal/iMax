# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='event_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
