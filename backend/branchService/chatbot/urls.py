#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yuande Liu <miraclecome (at) gmail.com>

from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('extract/', views.extract_time),
    path('admin/', admin.site.urls),
]
