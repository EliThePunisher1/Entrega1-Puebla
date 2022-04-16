from django.db import models

# Create your 
class modelo1(models.Model):
    nombre=models.CharField(max_length=10)
    apellido=models.CharField(max_length=10)
    contraseña=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return f"{self.nombre}{self.apellido}"
    
class modelo2(models.Model):
    nombre=models.CharField(max_length=10)
    apellido=models.CharField(max_length=10)
    contraseña=models.IntegerField()
    email=models.EmailField()
    
    def __str__(self):
        return f"{self.nombre}{self.apellido}"

class modelo3(models.Model):
    nombre=models.CharField(max_length=10)
    apellido=models.CharField(max_length=10)
    contraseña=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return f"{self.nombre}{self.apellido}"
    
    
    
    
    