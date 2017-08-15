# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FullName', models.CharField(max_length=50)),
                ('BirthDate', models.DateField()),
                ('Email', models.EmailField(unique=True, max_length=70)),
                ('Gender', models.CharField(max_length=1)),
                ('ProfilePic', models.ImageField(upload_to=b'')),
                ('Quote', models.CharField(max_length=200)),
                ('UserName', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
