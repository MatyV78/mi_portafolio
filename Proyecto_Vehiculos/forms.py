from django import forms
from Proyecto_Vehiculos.models import Vehiculo, VehiculoElec, VehiculoUsado, Marca, Modelo, Comentario, ComentarioUso, ComentarioElec






class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ["marca", "modelo", "año", "tipo_vehiculo","Precio"]        
        widgets = {
            "marca": forms.Select(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "año": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_vehiculo": forms.Select(attrs={"class": "form-control"}),
            "Precio": forms.TextInput(attrs={"class": "form-control"}),
        }
        
class VehiculoElecForm(forms.ModelForm):
    class Meta:
        model = VehiculoElec
        fields = ["marca", "modelo", "año", "tipo_vehiculo","Precio"]
        widgets = {
            "marca": forms.Select(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "año": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_vehiculo": forms.Select(attrs={"class": "form-control"}),
            "Precio": forms.TextInput(attrs={"class": "form-control"}),
        }
        
class VehiculoUsadoForm(forms.ModelForm):
    class Meta:
        model = VehiculoUsado
        fields = ["marca", "modelo", "año", "tipo_vehiculo","Precio"]
        widgets = {
            "marca": forms.Select(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "año": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_vehiculo": forms.Select(attrs={"class": "form-control"}),
            "Precio": forms.TextInput(attrs={"class": "form-control"}),
        }
        
        
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ["nombre_marca", "informacion_marca"]
        widgets = {
            "nombre_marca": forms.TextInput(attrs={"class": "form-control"}),
            "informacion_marca": forms.TextInput(attrs={"class": "form-control"}),
        }
    
class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ["marca", "modelo", "año"]
        widgets = {
            "marca": forms.Select(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "año": forms.TextInput(attrs={"class": "form-control"}),
        }  
        
        
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'texto']
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        
class ComentarioUsoForm(forms.ModelForm):
    class Meta:
        model = ComentarioUso
        fields = ['autor', 'texto']
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        
class ComentarioElecForm(forms.ModelForm):
    class Meta:
        model = ComentarioElec
        fields = ['autor', 'texto']
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }