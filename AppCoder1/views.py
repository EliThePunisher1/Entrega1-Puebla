from django.shortcuts import render

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

def BasePadre(request):
    plantillaBasePadre1=open(r'C:\Users\elipu\OneDrive\Escritorio\MiproyectoCoder\AppCoder1\Templates1\AppCoder11\BasePadre.html')
    template5=Template(plantillaBasePadre1.read())
    context5=Context()
    BasePadre1=template5.render(context5)
    return HttpResponse(BasePadre1)
