# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space_prospection', '0002_auto_20170824_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]