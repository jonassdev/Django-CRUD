from django.forms import ModelForm
from .models import Tasks

class TaskForm(ModelForm):
    class Meta:
        # Objeto creado con el modelo(tabla) a utilizar
        model = Tasks
        # Campos a utilizar
        fields = ['title' , 'description' ,'important']
        
class TaskDetailForm(ModelForm):
    class Meta:
        # Objeto creado con el modelo(tabla) a utilizar
        model = Tasks
        # Campos a utilizar
        fields = ['title']