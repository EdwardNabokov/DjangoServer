# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comics', '0007_auto_20170418_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimagemodel',
            name='pic',
            field=models.ImageField(upload_to='Media'),
        ),
    ]
