# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-04 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touchReader', '0005_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='content',
            field=models.TextField(null=True, verbose_name='\u5185\u5bb9'),
        ),
    ]
