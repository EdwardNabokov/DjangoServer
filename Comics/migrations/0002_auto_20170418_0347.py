# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='URL',
        ),
        migrations.AlterField(
            model_name='image',
            name='Image',
            field=models.URLField(),
        ),
    ]
