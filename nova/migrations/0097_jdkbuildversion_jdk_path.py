# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-05-17 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0096_jdkbuildversion'),
    ]

    operations = [
        migrations.AddField(
            model_name='jdkbuildversion',
            name='jdk_path',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='jdk\u8def\u5f84'),
        ),
    ]