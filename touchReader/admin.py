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

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Chapter)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(ImageUploader)

