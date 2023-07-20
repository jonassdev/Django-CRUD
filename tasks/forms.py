from django import forms
from .models import Tasks

class TaskForm(forms.ModelForm):
    class Meta:
        # Objeto creado con el modelo(tabla) a utilizar
        model = Tasks
        # Campos a utilizar
        fields = ['title' , 'description' ,'important']
        widgets = {
            'title' : forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Escribe un titulo' }),
            'description' : forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder' : 'Escribe una descripcion'
                }),
            'important' : forms.CheckboxInput(attrs={
                'class' : 'form-check-input m-auto '
                })     
        }
        