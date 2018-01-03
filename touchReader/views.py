# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from touchReader.models import User


def index(request):
    # User.objects.create(name="linguiwei", age=31, account="waynewgl", password="waynewgl")
    my_user = User.objects.filter(name="linguiwei")
    info_dict = {'site': u'自强学堂', 'content': my_user}

    return render(request, 'home.html', {'info_dict': info_dict})


def add(request, a, b):

    c = int(a) + int(b)
    return HttpResponse(str(c))