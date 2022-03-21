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



# Create your views here.

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

def Login(request):
    plantillalogin1=open(r"C:\Users\elipu\OneDrive\Escritorio\MiproyectoCoder\AppCoder1\Templates1\AppCoder11\Login.html")
    template6=Template(plantillalogin1.read())
    context6=Context()
    Login1=template6.render(context6)
    return HttpResponse(Login1)

# Formulario(request):
# print(request.method)
# if request.method== "POST":
#     print(request.POST)
#     nuevo_usuario=Usuarios(nombre=request.POST['Usuario'],Contraseña=Contraseña.POST['Contraseña'])
#     nuevo_usuario.save() 
#     return render(request,'AppCoder/Templates/Formulario.html',{'nuevo_usuario':nuevo_usuario})
      
# return render(request,'AppCoder/Templates/Formulario.html',{})



# if request.method == 'POST':
#     print(request.POST)
    
# formulario= Formulario()
# return render(request,'formulario.html',{'formulario:Formulario'})
