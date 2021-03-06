# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 17:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0020_auto_20161107_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='document',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 8, 17, 10, 53, 303635)),
        ),
        migrations.AlterField(
            model_name='document',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 8, 17, 10, 53, 303602)),
        ),
        migrations.AlterField(
            model_name='event',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 9, 17, 10, 53, 302301)),
        ),
        migrations.AlterField(
            model_name='images',
            name='Image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 8, 17, 10, 53, 301727)),
        ),
        migrations.AlterField(
            model_name='notes',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 8, 17, 10, 53, 301692)),
        ),
    ]
