# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 18:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20161102_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='Image',
        ),
        migrations.RemoveField(
            model_name='images',
            name='Image_tag',
        ),
        migrations.AddField(
            model_name='images',
            name='docfile',
            field=models.FileField(default=django.utils.timezone.now, upload_to=b'documents/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
