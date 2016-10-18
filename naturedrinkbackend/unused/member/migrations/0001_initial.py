# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-03 16:42
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=100)),
                ('road', models.CharField(max_length=100)),
                ('sub_district', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('zipcode', models.PositiveIntegerField(max_length=5, validators=[django.core.validators.MinLengthValidator(5)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]