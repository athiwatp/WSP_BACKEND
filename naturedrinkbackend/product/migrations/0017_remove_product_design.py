# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 17:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20161115_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='design',
        ),
    ]