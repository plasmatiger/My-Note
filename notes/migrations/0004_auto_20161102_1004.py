# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='Image',
            field=models.ImageField(upload_to=b'notes/files'),
        ),
    ]
