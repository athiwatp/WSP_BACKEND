# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zipcode',
            field=models.CharField(max_length=6),
        ),
    ]