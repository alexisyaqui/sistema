from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.utils.decorators import method_decorator

from app_clinica.forms import PacienteForm
from app_clinica.models import Paciente

class PacientelistaListView(ListView):
    model = Paciente
    template_name = 'paciente/paciente_list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Paciente.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Pacientes'
        context['crearpac_url'] = reverse_lazy('paciente_registro')
        context['listapac_url'] = reverse_lazy('paciente_lista')
        context['entidad'] = 'Pacientes'
        return context


class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/paciente_registro.html'
    success_url = reverse_lazy('paciente_lista')

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
        context['title'] = 'Registro de Paciente'
        context['entidad'] = 'Pacientes'
        context['listapac_url'] = reverse_lazy('paciente_lista')
        context['action'] = 'registro'
        return context


class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/paciente_registro.html'
    success_url = reverse_lazy('paciente_lista')

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
        context['title'] = 'Editar Paciente'
        context['entidad'] = 'Pacientes'
        context['listapac_url'] = reverse_lazy('paciente_lista')
        context['action'] = 'editar'
        return context


class PacineteDeleteView(DeleteView):
    model = Paciente
    template_name = 'paciente/paciente_eliminar.html'
    success_url = reverse_lazy('paciente_lista')

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
        context['title'] = 'Eliminar Paciente'
        context['entidad'] = 'Pacientes'
        context['listapac_url'] = reverse_lazy('paciente_lista')

        return context


class PacienteFormView(FormView):
    form_class = PacienteForm
    template_name = 'paciente/paciente_registro.html'
    success_url = reverse_lazy('paciente_lista')

    def form_valid(self, form):
        print(form.is_valid())
        print(form)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.is_valid())
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Form | Paciente'
        context['entidad'] = 'Pacientes'
        context['listapac_url'] = reverse_lazy('paciente_lista')
        context['action'] = 'registrar'
        return context
