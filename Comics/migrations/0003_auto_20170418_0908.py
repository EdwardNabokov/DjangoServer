# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comics', '0002_auto_20170418_0347'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='URL',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='Image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
