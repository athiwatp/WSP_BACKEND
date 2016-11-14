# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DesignBottle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='DesignRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_confirm', models.BooleanField(default=False)),
                ('price', models.FloatField(default=None, null=True)),
                ('bottle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='design.DesignBottle')),
            ],
        ),
    ]
