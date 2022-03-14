from django.http import HttpResponse
from django.template import Context, Template


def Titulo(request):
    return HttpResponse("Aca van los titulos que queramos agregar")

def Plantilla(request):
    plantillabase=open(r"C:\Users\elipu\OneDrive\Escritorio\MiproyectoCoder\ProyectoCoder\Plantillas\Plantillas.HTML")
    template=Template(plantillabase.read())
    context=Context()
    plantilla_1=template.render(context)
    return HttpResponse(plantilla_1)


def Perfil1(request):
    return HttpResponse("Perfil1")


def Perfil2(request):
    return HttpResponse("Perfil2")


def Perfil3(request):
    return HttpResponse("Perfil3")

def Perfil4(request):
    return HttpResponse("Perfil4")