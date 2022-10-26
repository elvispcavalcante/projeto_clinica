from django.urls import path
from .views import CadastroPaciente

app_name = 'clinica'

urlpatterns = [
    path('cadastro_paciente/', CadastroPaciente.as_view(), name='cadastro_paciente'),
]
