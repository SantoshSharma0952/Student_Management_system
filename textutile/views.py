# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 01:02:31 2021

@author: santosh.sharma
"""

#I have created this file - Santosh

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse("About Blog")

