from django.views.generic import  TemplateView

class DashboadView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['panel'] = 'Panel de administrador'