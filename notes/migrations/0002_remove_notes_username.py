# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 04:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='UserName',
        ),
    ]
