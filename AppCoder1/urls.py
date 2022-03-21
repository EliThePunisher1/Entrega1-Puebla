from django.contrib import admin
from django.urls import path
from .views import Inicio,Contacto,SobreNosotros,Historia

urlpatterns = [path('admin/', admin.site.urls),
               path('',Inicio),
               path('Inicio/',Inicio),
               path('Contacto/',Contacto),
               path('Historia/',Historia),
               path('SobreNosotros/',SobreNosotros)]
