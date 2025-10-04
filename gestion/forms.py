from django import forms
from .models import Colegio

class RegistroColegioForm(forms.ModelForm):
    """Formulario para el registro de un nuevo colegio y su usuario asociado."""
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    # Campo para el correo electrónico, que será el identificador del usuario
    email = forms.EmailField(label="Correo Electrónico de Contacto")

    class Meta:
        model = Colegio
        # Solo pedimos los campos del colegio, el usuario se creará por detrás
        fields = ['nombre', 'codigo_dane', 'ubicacion']
        labels = {
            'nombre': 'Nombre de la Institución',
            'codigo_dane': 'Código DANE',
            'ubicacion': 'Ubicación (Ciudad, Departamento)',
        }

class LoginForm(forms.Form):
    """Formulario de inicio de sesión para los colegios."""
    username = forms.CharField(label="Nombre de la Institución o Código DANE", max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")


class SubirArchivoForm(forms.Form):
    archivo_csv = forms.FileField(label="Selecciona un archivo CSV")
