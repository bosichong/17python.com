# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-02 02:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Siteinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='', max_length=20, verbose_name='站点名称')),
                ('site_detail', models.CharField(default='', max_length=100, verbose_name='站点介绍')),
                ('site_footer', models.TextField(default='', verbose_name='站点底部代码')),
                ('site_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='管理员')),
            ],
            options={
                'verbose_name': '网站信息',
                'verbose_name_plural': '网站信息',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='article_synopsis',
            field=models.TextField(default='', verbose_name='日志简介'),
        ),
        migrations.AddField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='category',
            name='daitail',
            field=models.CharField(default='', max_length=100, verbose_name='分类介绍'),
        ),
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(default='', max_length=100, verbose_name='分类图标'),
        ),
        migrations.AddField(
            model_name='category',
            name='sort_id',
            field=models.IntegerField(default=99, verbose_name='分类排序'),
        ),
    ]
