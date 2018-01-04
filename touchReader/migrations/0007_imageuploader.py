# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-04 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('touchReader', '0006_auto_20180104_0745'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUploader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='upload')),
                ('article', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='touchReader.Article')),
            ],
        ),
    ]
