from contextlib import ContextDecorator
from contextvars import Context
from ctypes.wintypes import tagMSG
from curses.ascii import HT
from pipes import Template
from re import template
from tempfile import tempdir
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template
# Create your views here.

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def sobrenosotros(request):
    return render(request,"AppCoder/sobrenosotros.html")

def contacto(request):
    return HttpResponse(request,"AppCoder/contacto.html")

def novedades(request):
    return HttpResponse(request,"AppCoder/novedades.html")



