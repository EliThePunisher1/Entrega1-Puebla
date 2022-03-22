from django.db import models

# Create your 
class modelo1(models.Model):
    nombre=models.CharField(max_length=10)
    apellido=models.IntegerField()
    contraseña=models.IntegerField()
    email=models.EmailField()
    
class modelo2(models.Model):
    nombre=models.CharField(max_length=10)
    apellido=models.IntegerField()
    contraseña=models.IntegerField()
    email=models.EmailField()
    
    
    
    
    