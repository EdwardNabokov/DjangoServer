# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comics', '0003_auto_20170418_0908'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='pictures')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
