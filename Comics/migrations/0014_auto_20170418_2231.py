# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comics', '0013_auto_20170418_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadimagemodel',
            name='pic',
        ),
        migrations.AddField(
            model_name='uploadimagemodel',
            name='image',
            field=models.FileField(default=0, upload_to='media/pictures'),
            preserve_default=False,
        ),
    ]
