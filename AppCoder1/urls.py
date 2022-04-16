from django.urls import path
from .views import inicio, sobrenosotros, contacto, novedades, formularios
from .views import buscar,nohaynada
urlpatterns = [
    path('', inicio),
    path('inicio/',inicio),
    path('contacto/', contacto),
    path('sobrenosotros/', sobrenosotros),
    path('novedades/', novedades),
    path('formulario/',formularios),
    path('buscar/',buscar),
    path('error/',nohaynada),
]



