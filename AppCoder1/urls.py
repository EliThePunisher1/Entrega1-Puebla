from django.urls import path
from .views import inicio, sobrenosotros, contacto, novedades

urlpatterns = [
    path('', inicio),
    path('contacto/', contacto),
    path('sobrenosotros/', sobrenosotros),
    path('novedades/', novedades)
]



