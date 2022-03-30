from django.http import HttpResponse
from django.shortcuts import render
from .models import modelo1
from AppCoder1.forms import formulario

# Create your views here.


def inicio(request):
    return render(request,"AppCoder/inicio.html")

def sobrenosotros(request):
    return render(request,"AppCoder/sobrenosotros.html")

def contacto(request):
    return render(request,"AppCoder/contacto.html")

def novedades(request):
    return render(request,"AppCoder/novedades.html")


def formularios(request):
    if request.method == 'POST':
        miformulario=formulario(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion=miformulario.cleaned_data
            usuario=modelo1(informacion['nombre'],informacion['apellido'],informacion['email'],informacion['contraseña'])
            usuario.save()
            return render(request,"AppCoder/inicio.html",{'usuario':usuario})
    else:
        miformulario=formulario()
    return render(request,'AppCoder/formulario.html',{'formulario':miformulario})
