# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comics', '0014_auto_20170418_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimagemodel',
            name='image',
            field=models.FileField(upload_to='pictures'),
        ),
    ]
