# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-07 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_blogimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.CharField(default='', max_length=50, verbose_name='日志标签'),
        ),
    ]
