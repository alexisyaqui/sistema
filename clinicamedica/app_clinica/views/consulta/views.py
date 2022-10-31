from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from app_clinica.forms import PacienteForm, MedicoForm, ConsultaMedicaForm
from app_clinica.models import Paciente, Medico, Consulta


class ConsultaMedicaListView(ListView):
    model = Consulta
    template_name = 'consulta/consulta_lista.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consultas'
        context['crearpac_url'] = reverse_lazy('consulta_registro')
        context['listapac_url'] = reverse_lazy('consulta_lista')
        context['entidad'] = 'Consulta Medica'
        return context


class CrearConsultaCreateView(CreateView):
    model = Consulta
    form_class = ConsultaMedicaForm
    template_name = 'consulta/consulta_registro.html'
    success_url = reverse_lazy('consulta_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'registro':
                form = self.get_form()
                data = form.save()
            else:
                data['error']: 'no ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro Consulta'
        context['entidad'] = 'Consulta'
        context['listapac_url'] = reverse_lazy('consulta_lista')
        context['action'] = 'registro'
        return context


class ConsultaUpdateView(UpdateView):
    model = Consulta
    form_class = ConsultaMedicaForm
    template_name = 'consulta/consulta_registro.html'
    success_url = reverse_lazy('consulta_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'editar':
                form = self.get_form()
                data = form.save()
            else:
                data['error']: 'no ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Consulta'
        context['entidad'] = 'Consulta'
        context['listapac_url'] = reverse_lazy('consulta_lista')
        context['action'] = 'editar'
        return context


class ConsultaDeleteView(DeleteView):
    model = Consulta
    template_name = 'consulta/consulta_eliminar.html'
    success_url = reverse_lazy('consulta_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Consulta'
        context['entidad'] = 'Consulta'
        context['listapac_url'] = reverse_lazy('consulta_lista')

        return context
