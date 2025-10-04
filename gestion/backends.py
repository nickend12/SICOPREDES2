from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import Usuario, Colegio

class ColegioBackend(ModelBackend):
    """
    Backend de autenticación personalizado para permitir el inicio de sesión
    con el nombre del colegio o el código DANE.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Sobrescribe el método authenticate para buscar al usuario a través del colegio.
        """
        try:
            # Busca un colegio que coincida con el nombre o el código DANE
            colegio = Colegio.objects.get(Q(nombre__iexact=username) | Q(codigo_dane__iexact=username))
            # Si se encuentra el colegio, se obtiene el usuario asociado
            user = colegio.usuario
        except Colegio.DoesNotExist:
            # Si no se encuentra un colegio, no se puede autenticar
            return None

        # Se verifica la contraseña del usuario encontrado
        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        """
        Sobrescribe el método get_user para obtener un usuario por su ID.
        """
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
