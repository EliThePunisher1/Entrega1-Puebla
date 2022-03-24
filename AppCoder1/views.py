from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def sobrenosotros(request):
    return render(request,"AppCoder/sobrenosotros.html")

def contacto(request):
    return HttpResponse(request,"AppCoder/contacto.html")

def novedades(request):
    return HttpResponse(request,"AppCoder/novedades.html")



