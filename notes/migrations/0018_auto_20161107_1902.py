# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 19:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0017_auto_20161105_0634'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 7, 19, 2, 34, 378484)),
        ),
        migrations.AddField(
            model_name='document',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 7, 19, 2, 34, 378454)),
        ),
        migrations.AddField(
            model_name='notes',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 7, 19, 2, 34, 375543)),
        ),
        migrations.AlterField(
            model_name='event',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 8, 19, 2, 34, 376080)),
        ),
        migrations.AlterField(
            model_name='notes',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 7, 19, 2, 34, 375516)),
        ),
    ]
