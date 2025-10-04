from django.contrib.auth.models import AbstractUser
from django.db import models


class Colegio(models.Model):
    """Representa una institución educativa."""
    id_colegio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    codigo_dane = models.CharField(
        max_length=225, unique=True, help_text="Código DANE de la institución"
    )
    ubicacion = models.CharField(max_length=255)
    num_estudiantes = models.IntegerField(default=0)
    num_docentes = models.IntegerField(default=0)
    usuario = models.OneToOneField(
        'Usuario',
        on_delete=models.CASCADE,
        related_name='colegio_asociado',
        null=True,  # Permitir nulos temporalmente durante la migración
        blank=True
    )

    class Meta:
        verbose_name = "Colegio"
        verbose_name_plural = "Colegios"

    def __str__(self):
        return self.nombre



class Usuario(AbstractUser):
    """Modelo de usuario personalizado para la autenticación."""
    # Usaremos el email como principal forma de identificación, en lugar del username.
    email = models.EmailField('correo electrónico', unique=True)
    # Hacemos que el campo username, heredado de AbstractUser, sea opcional.
    username = models.CharField(
        'nombre de usuario',
        max_length=150,
        unique=True,
        blank=True,  # Permitimos que el campo esté en blanco
        null=True    # Y que sea nulo en la base de datos
    )

    # Definimos el email como el campo para el login
    USERNAME_FIELD = 'email'
    # Campos requeridos al crear un superusuario por consola (además de email y password)
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Estudiante(models.Model):
    """Representa a un estudiante inscrito en un colegio."""
    id_estudiante = models.AutoField(primary_key=True)
    colegio = models.ForeignKey(
        Colegio, on_delete=models.CASCADE, db_column="id_colegio", related_name="estudiantes"
    )
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=255)  # en el diagrama no es limitado a M/F
    grado = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class Asistencia(models.Model):
    """Registra la asistencia de un estudiante en una fecha específica."""
    id_asistencia = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(
        Estudiante, on_delete=models.CASCADE, db_column="id_estudiante", related_name="asistencias"
    )
    fecha = models.DateField()
    estado = models.BooleanField(default=True, help_text="True = presente, False = ausente")

    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"
        unique_together = ("estudiante", "fecha")

    def __str__(self):
        return f"Asistencia de {self.estudiante} el {self.fecha}: {'Presente' if self.estado else 'Ausente'}"
