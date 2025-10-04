# Incluye las URLs de la app gestion
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # URLs de autenticación para colegios
    path('registro/', views.registro_colegio, name='registro_colegio'),
    path('login/', views.login_colegio, name='login_colegio'),
    path('logout/', views.custom_logout, name='logout_colegio'),

    path('colegio/<int:id_colegio>/subir-archivo/', views.subir_archivo, name='subir_archivo'),
    path('colegio/<int:id_colegio>/dashboard/', views.dashboard_colegio, name='dashboard_colegio'),
]
