from django.http import HttpResponse
from django.shortcuts import render
from .models import modelo1,modelo3
from AppCoder1.forms import formulario, buscar

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
            usuario=modelo1(informacion['identificacion'],informacion['nombre'],informacion['apellido'],informacion['contraseña'],informacion['email'])
            usuario.save()
            return render(request,"AppCoder/inicio.html",{'usuario':usuario})
    else:
        miformulario=formulario()
    return render(request,'AppCoder/formulario.html',{'formulario':miformulario})

def buscar1(request):
    usuario_buscado=[]
    dato=request.GET.get('nombre',None)
    if dato is not None:
        usuario_buscado=modelo1.objects.filter(modelo1__icontains=dato)    
    buscador= buscar()
    return render(request,"AppCoder/busquedausuarios.html",{'buscador':buscador,'usuario_buscado':usuario_buscado})



def nohaynada(request):
    return render(request, 'AppCoder/nohaynada.html')