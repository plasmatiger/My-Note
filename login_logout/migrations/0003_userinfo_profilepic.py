# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login_logout', '0002_remove_userinfo_profilepic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='ProfilePic',
            field=models.ImageField(default=datetime.datetime(2016, 11, 4, 7, 7, 24, 693482, tzinfo=utc), upload_to=b'ProfilePic/'),
            preserve_default=False,
        ),
    ]
