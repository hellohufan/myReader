# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from touchReader.models import User
from touchReader.models import Article

import logging
logger = logging.getLogger("django")  # 为loggers中定义的名称


def index(request):
    # User.objects.create(name="linguiwei", age=31, account="waynewgl", password="waynewgl")
    #my_user = User.objects.filter(name="linguiwei")

    new_article = Article.objects.filter(id=1)

    # logger.info("some info...", new_article[0].title)

    return render(request, 'home.html', {'info_dict': new_article[0]})


def add(request, a, b):

    c = int(a) + int(b)
    return HttpResponse(str(c))


