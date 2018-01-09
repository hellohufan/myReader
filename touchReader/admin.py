# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Book
from .models import Publisher
from .models import Chapter
from .models import Article
from .models import User
from .models import Tag
from .models import ImageUploader

# Register your models here.

class MyAdminSite(admin.AdminSite):
    site_header = '阅犀后台管理系统'  # 此处设置页面显示标题
    site_title = '阅犀'  # 此处设置页面头部标题


admin.site = MyAdminSite(name='management')

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Chapter)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(ImageUploader)



