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

def Formulario(request):
    if request.method== "POST":
        nuevo_usuario=Usuarios(request.POST['Usuario'],request.POST['Contraseña'])
        nuevo_usuario.save() 
        return render(request,'C:\Users\elipu\OneDrive\Escritorio\MiproyectoCoder\AppCoder1\Templates1\AppCoder11\Inicio.html')
    return render(request,"C:\Users\elipu\OneDrive\Escritorio\MiproyectoCoder\AppCoder1\Templates1\AppCoder11\Formulario.html")

def Formulario(request):
    if request.method=="POST":
        miformulario=NuevosUsuarios(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion=miformulario.cleaned_data
            usuarios=Usuarios(nombre=informacion['usuario'],contaseña=informacion['contraseña'])
            usuarios.save()
            return render(request,'C:\Users\elipu\OneDrive\Escritorio\MiproyectoCoder\AppCoder1\Templates1\AppCoder11\Inicio.html')
        
    else:
        miformulario=NuevosUsuarios()
        return render(request,'C:\Users\elipu\OneDrive\Escritorio\MiproyectoCoder\AppCoder1\Templates1\AppCoder11\Formulario.html',{"miformulario":miformulario})
    

# def busquedausuarios(request):
#     return render(request,'C:\Users\elipu\OneDrive\Escritorio\MiproyectoCoder\AppCoder1\Templates1\busquedausuarios.html')

def buscar(request):
     if request.GET["usuario"]:
         
         usuario=request.GET["usuario"]
         contraseña=usuario.objects.filter(usuario__icontains=usuario)
         
         return render(request,"C:\Users\elipu\OneDrive\Escritorio\MiproyectoCoder\AppCoder1\Templates1\busquedausuarios.html",{"Usuarios":usuario, "contraseña":contraseña})
     else:
        respuesta="no enviaste datos"
         
        return HttpResponse(respuesta)
