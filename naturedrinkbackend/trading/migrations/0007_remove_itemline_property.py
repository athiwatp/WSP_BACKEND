# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 19:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0006_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemline',
            name='property',
        ),
    ]
