from django.views.generic import TemplateView

from app_clinica.models import Nombre_Clinica


class IndexView(TemplateView):
    model = Nombre_Clinica
    template_name = 'inicio_pag.html'


    