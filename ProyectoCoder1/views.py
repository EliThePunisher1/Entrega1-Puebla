from contextlib import ContextDecorator
from contextvars import Context
from ctypes.wintypes import tagMSG
from pipes import Template
from re import template
from tempfile import tempdir
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template

   


# Este archivo views es para generar nuestras vistas, y pasarlas a html. Desde aca despues conecta urls !!!!!!!!!!!




# def Titulo(request):
#     return HttpResponse("Aca van los titulos que queramos agregar")

# def Plantilla(request):
#     plantillabase=open(r"C:\Users\elipu\OneDrive\Escritorio\MiproyectoCoder\ProyectoCoder\Plantillas\Plantillas.HTML")
#     template=Template(plantillabase.read())
#     context=Context()
#     plantilla_1=template.render(context)
#     return HttpResponse(plantilla_1)


# def Perfil1(request):
#     return HttpResponse("Perfil1")


# def Perfil2(request):
#     return HttpResponse("Perfil2")


# def Perfil3(request):
#     return HttpResponse("Perfil3")

# def Perfil4(request):
#     return HttpResponse("Perfil4")


def Formulario(request):
    plantillabase1=open(r"C:\Users\elipu\OneDrive\Escritorio\MiproyectoCoder\AppCoder1\Templates1\AppCoder11\Formulario.html")
    template=Template(plantillabase1.read())
    context=Context()
    Formulario=template.render(context)
    return HttpResponse(Formulario)

def Inicio(request):
    plantillaincio1=open(r"C:\Users\elipu\OneDrive\Escritorio\MiproyectoCoder\AppCoder1\Templates1\AppCoder11\Inicio.html")
    template1=Template(plantillaincio1.read())
    context1=Context()
    Inicio1=template1.render(context1)
    return HttpResponse(Inicio1)

def Historia(request):
    plantillabasehistoria1=open(r'C:\Users\elipu\OneDrive\Escritorio\MiproyectoCoder\AppCoder1\Templates1\AppCoder11\Historia.html')
    template2=Template(plantillabasehistoria1.read())
    context2=Context()
    Historia1=template2.render(context2)
    return HttpResponse(Historia1)

def SobreNosotros(request):
    plantillaSobreNosotros1=open(r'C:\Users\elipu\OneDrive\Escritorio\MiproyectoCoder\AppCoder1\Templates1\AppCoder11\Sobre Nosotros.html')
    template3=Template(plantillaSobreNosotros1.read())
    context3=Context()
    SobreNosotros1=template3.render(context3)
    return HttpResponse(SobreNosotros1)

def Contacto(request):
    plantillaContacto1=open(r'C:\Users\elipu\OneDrive\Escritorio\MiproyectoCoder\AppCoder1\Templates1\AppCoder11\Contacto.html')
    template4=Template(plantillaContacto1.read())
    context4=Context()
    Contacto1=template4.render(context4)
    return HttpResponse(Contacto1)