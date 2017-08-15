# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_notes_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='UserName',
            field=models.CharField(max_length=20),
        ),
    ]
