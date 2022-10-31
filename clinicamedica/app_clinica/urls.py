from django.urls import path
from app_clinica.views.paciente.views import *
from app_clinica.views.medico.views import *
from app_clinica.views.consulta.views import *

from app_clinica.views.dashboard.views import *


urlpatterns = [
    #urls de los pacientes
    path('paciente/lista/', PacientelistaListView.as_view(), name='paciente_lista'),
    path('paciente/registro/', PacienteCreateView.as_view(), name='paciente_registro'),
    path('paciente/editar/<int:pk>/', PacienteUpdateView.as_view(), name='paciente_editar'),
    path('paciente/eliminar/<int:pk>/', PacineteDeleteView.as_view(), name='paciente_eliminar'),
    path('paciente/form', PacienteFormView.as_view(), name='paciente_form'),

    #urls de dashboard
    path('dashboard/', DashboadView.as_view(), name='dashboard'),

    # urls de los Medicos
    path('medico/lista/', MedicoListView.as_view(), name='medico_lista'),
    path('medico/registro/', MedicoCreateView.as_view(), name='medico_registro'),
    path('medico/editar/<int:pk>/', MedicoUpdateView.as_view(), name='medico_editar'),
    path('medico/eliminar/<int:pk>/', MedicoDeleteView.as_view(), name='medico_eliminar'),

    # urls de consulta
    path('consulta/lista/', ConsultaMedicaListView.as_view(), name='consulta_lista'),
    path('consulta/registro/', CrearConsultaCreateView.as_view(), name='consulta_registro'),
    path('consulta/editar/<int:pk>/', ConsultaUpdateView.as_view(), name='consulta_editar'),
    path('consulta/eliminar/<int:pk>/', ConsultaDeleteView.as_view(), name='consulta_eliminar'),

]
