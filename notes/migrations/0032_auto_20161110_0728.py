# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 07:28
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0031_auto_20161110_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='UserName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='document',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 10, 7, 28, 59, 412134)),
        ),
        migrations.AlterField(
            model_name='document',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 10, 7, 28, 59, 412104)),
        ),
        migrations.AlterField(
            model_name='event',
            name='UserName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 11, 7, 28, 59, 409590)),
        ),
        migrations.AlterField(
            model_name='images',
            name='UserName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notes',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 10, 7, 28, 59, 408937)),
        ),
        migrations.AlterField(
            model_name='notes',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 10, 7, 28, 59, 408896)),
        ),
    ]
