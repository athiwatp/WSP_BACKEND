# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 07:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0004_auto_20161115_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designrequest',
            name='bottle',
        ),
        migrations.RemoveField(
            model_name='designrequest',
            name='user',
        ),
        migrations.DeleteModel(
            name='DesignRequest',
        ),
    ]
