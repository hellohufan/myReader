# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    age = models.IntegerField()
    mobile = models.CharField(max_length=50, verbose_name=u"手机号码", default="")

    def __unicode__(self):
        # 在Python3中使用 def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=20)


class Book(models.Model):
    name = models.CharField(max_length=20)
    pub = models.ForeignKey(Publisher)
    authors = models.ManyToManyField(User)