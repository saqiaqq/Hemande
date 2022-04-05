# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:saqia  time:2022/4/5
from django.urls import path, re_path

from index import views

urlpatterns = [
    path('', views.index_view),
    path('<year>/<int:month>/<slug:day>', views.mydate),
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='myyear'),
    re_path('dict/(?P<year>[0-9]{4}).htm', views.myyear_dict, {'month': '05'}, name='myyear_dict'),
]
