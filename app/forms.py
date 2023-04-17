from django import forms
from .models import Profesor

# El formulario hereda las validaciones definidas en el modelo.
class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'
        # fields = ['nombre', 'apellidos', 'email', 'mensaje', 'fecha']  # Otra forma
