# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 17:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0021_auto_20161108_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 8, 17, 24, 26, 928901)),
        ),
        migrations.AlterField(
            model_name='document',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 8, 17, 24, 26, 928872)),
        ),
        migrations.AlterField(
            model_name='event',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 9, 17, 24, 26, 927822)),
        ),
        migrations.AlterField(
            model_name='notes',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 8, 17, 24, 26, 927316)),
        ),
        migrations.AlterField(
            model_name='notes',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 8, 17, 24, 26, 927280)),
        ),
    ]
