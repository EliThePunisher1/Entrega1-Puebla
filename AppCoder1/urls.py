from django.urls import path
from .views import inicio, sobrenosotros, contacto, novedades, miformulario
urlpatterns = [
    path('', inicio),
    path('inicio/',inicio),
    path('contacto/', contacto),
    path('sobrenosotros/', sobrenosotros),
    path('novedades/', novedades),
    path('formulario/',miformulario),
]



