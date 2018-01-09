# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    age = models.IntegerField()
    mobile = models.CharField(max_length=50, verbose_name=u"手机号码", default="")

    def __str__(self):
        # 在Python3中使用 def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=20)
    # 一本书只有一个出版社
    pub = models.ForeignKey(Publisher)
    # 一本书只有可以有多个作者， 一个作者多本书
    authors = models.ManyToManyField(User)

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.name


class Chapter(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
    book = models.ForeignKey(Book)

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.title + "[" + self.book.name + "]"


class ImageUploader(models.Model):
    img = models.ImageField(upload_to='upload')
    # article = models.ForeignKey(Article, default="")

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.img.url


class Tag(models.Model):
    title = models.CharField(u'标签标题', max_length=256)
    content = models.TextField(u'内容', null=True)
    # article = models.ManyToManyField(Article)

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.title


class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
    chapter = models.ForeignKey(Chapter)
    images = models.ManyToManyField(ImageUploader)
    tags = models.ManyToManyField(Tag)

    # 仅修改 content 字段
    content = UEditorField('内容', height=300, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.title + " " + self.chapter.title + "-" + "[" + self.chapter.book.name + "]" + " "




