# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space_prospection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('post_pic', models.ImageField(null=True, upload_to='')),
                ('post_title', models.CharField(max_length=100)),
                ('post_pub_date', models.DateTimeField(verbose_name='date published')),
                ('post_content', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('proj_title', models.CharField(max_length=100)),
                ('proj_pic', models.ImageField(null=True, upload_to='')),
                ('proj_content', models.TextField(default='')),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
