# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 06:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0016_auto_20161104_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 6, 6, 34, 15, 928375)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='notes',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 6, 6, 34, 15, 927741)),
        ),
    ]
