# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comics', '0004_auto_20170418_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimagemodel',
            name='pic',
            field=models.ImageField(upload_to='~/WebServerComics/Comics/pictures'),
        ),
    ]
