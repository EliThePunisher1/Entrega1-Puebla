from django.http import HttpResponse
from django.shortcuts import render
from .models import modelo1
# from .forms import formulario
# Create your views here.
def inicio(request):
    return render(request,"AppCoder/inicio.html")

def sobrenosotros(request):
    return render(request,"AppCoder/sobrenosotros.html")

def contacto(request):
    return HttpResponse(request,"AppCoder/contacto.html")

def novedades(request):
    return HttpResponse(request,"AppCoder/novedades.html")

def miformulario(request):
    if request.method=="POST":
        usuarios=modelo1(request.POST['nombre'],request.POST['apellido'],request.POST['contraseña'],request.POST['email'])
        usuarios.save()
        return render(request,"AppCoder/inicio.html")
    return render(request,"AppCoder/formulario.html")

