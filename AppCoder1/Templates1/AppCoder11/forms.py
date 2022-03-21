from django import forms

class NuevosUsuarios(forms.Form):
    Usuario=forms.CharField(max_length=20)
    Constraseña=forms.IntegerField(max_length=20)
    