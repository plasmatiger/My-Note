# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0020_auto_20161107_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 9, 17, 14, 22, 252858)),
        ),
        migrations.AlterField(
            model_name='document',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 9, 17, 14, 22, 252831)),
        ),
        migrations.AlterField(
            model_name='event',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 10, 17, 14, 22, 251465)),
        ),
        migrations.AlterField(
            model_name='notes',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 9, 17, 14, 22, 250888)),
        ),
        migrations.AlterField(
            model_name='notes',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 9, 17, 14, 22, 250855)),
        ),
    ]
