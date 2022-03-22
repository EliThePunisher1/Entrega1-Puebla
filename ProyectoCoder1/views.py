from contextlib import ContextDecorator
from contextvars import Context
from ctypes.wintypes import tagMSG
from pipes import Template
from re import template
from tempfile import tempdir
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template
from django.template import loader

# Create your views here.
#estas son vistas
# def saludo(request):
#     return HttpResponse("Hola!")

# def saludo2(request):
#     return HttpResponse("Hola como va?")


# estas son vistas traidas de un archivo html

# def primertemplate(request):
#     template1=open(r"ProyectoCoder1/plantillas/template1.html")
        
#     plantilla=Template(template1.read())
        
#     contexto=Context()

#     documento=plantilla.render(contexto)
#     return HttpResponse(documento)

# estas son vistas que trabajan con diccionarios

# def probandodiccionarios(self):
#     nombre="pepito"
#     apellido="lozano"
#     edad="24"
    
#     diccionario={"nombre":nombre, "apellido":apellido,"edad":edad,}
#     mihtml=(r"plantillas/template1.html")
#     plantilla=Template(mihtml.read())
#     mihtml.close()
#     contexto=Context(diccionario)
#     documento=plantilla.render(contexto)
#     return HttpResponse(documento)

# esta es otra forma de trabajar con diccionarios


# def otrodiccionario(request):
#     nombre="pepito"
#     apellido="lozano"
#     edad="24"
#     diccionario = {"nombre": nombre, "apellido": apellido, "edad": edad}
#     plantilla=loader.get_template("plantillas/template1.html")
#     documento=plantilla.render(diccionario)
#     return HttpResponse(documento)
    
# ACA PODEMOS EMPEZAR A GENERAR NUESTRAS VIEWS





