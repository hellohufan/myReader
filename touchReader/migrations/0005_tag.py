# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-04 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touchReader', '0004_auto_20180104_0716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='\u6807\u7b7e\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('article', models.ManyToManyField(to='touchReader.Article')),
            ],
        ),
    ]
