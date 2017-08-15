# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0011_auto_20161104_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='Note',
            field=models.TextField(),
        ),
    ]
