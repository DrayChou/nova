# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-30 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0023_auto_20170926_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('comment', models.CharField(blank=True, max_length=160, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='appconfig',
            name='files',
            field=models.CharField(max_length=300, verbose_name='\u914d\u7f6e\u6587\u4ef6'),
        ),
        migrations.AlterField(
            model_name='appconfig',
            name='svn_url',
            field=models.CharField(max_length=200, null=True, verbose_name='SVN\u8def\u5f84'),
        ),
        migrations.AddField(
            model_name='app',
            name='appgroups',
            field=models.ManyToManyField(blank=True, to='nova.AppGroup', verbose_name='\u6240\u5c5e\u5e94\u7528\u7ec4'),
        ),
    ]
