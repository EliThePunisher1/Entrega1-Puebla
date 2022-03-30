from django import forms

class formulario(forms.Form):
    nombre= forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    contraseña=forms.IntegerField()
    email=forms.CharField(max_length=50)