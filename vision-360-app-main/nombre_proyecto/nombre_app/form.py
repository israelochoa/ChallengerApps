from django import forms
from .models import Campus, Facultad, Bloque

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['nombre', 'descripcion', 'estado', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control-file'})
            
        }


class FacultadForm(forms.ModelForm):
    class Meta:
        model = Facultad
        fields = ['nombre', 'siglas', 'ubicacion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'siglas': forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacion': forms.URLInput(attrs={'class': 'form-control'}),
        }


class BloqueForm(forms.ModelForm):
    class Meta:
        model = Bloque
        fields = ['codigo_identificativo','nombre', 'campus', 'descripcion', 'estado', 'imagen', 'link']
        widgets = {
            'codigo_identificativo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'campus': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control-file'}),
            'link': forms.URLInput(attrs={'class': 'form-control'})
        }

