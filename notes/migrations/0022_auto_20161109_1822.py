# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0021_auto_20161109_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 9, 18, 22, 49, 677007)),
        ),
        migrations.AlterField(
            model_name='document',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 9, 18, 22, 49, 676979)),
        ),
        migrations.AlterField(
            model_name='event',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 10, 18, 22, 49, 675596)),
        ),
        migrations.AlterField(
            model_name='notes',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 9, 18, 22, 49, 674941)),
        ),
        migrations.AlterField(
            model_name='notes',
            name='my_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 9, 18, 22, 49, 674909)),
        ),
    ]
