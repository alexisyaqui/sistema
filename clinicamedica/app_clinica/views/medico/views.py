from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from app_clinica.forms import MedicoForm
from app_clinica.models import Medico


class MedicoListView(ListView):
    model = Medico
    template_name = 'medico/medico_list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Medicos'
        context['crearpac_url'] = reverse_lazy('medico_registro')
        context['listapac_url'] = reverse_lazy('medico_lista')
        context['entidad'] = 'Medicos'
        return context


class MedicoCreateView(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico/medico_registro.html'
    success_url = reverse_lazy('medico_lista')

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
        context['title'] = 'Registro Medico'
        context['entidad'] = 'Medico'
        context['listapac_url'] = reverse_lazy('medico_lista')
        context['action'] = 'registro'
        return context


class MedicoUpdateView(UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico/medico_registro.html'
    success_url = reverse_lazy('medico_lista')

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
        context['title'] = 'Editar Medico'
        context['entidad'] = 'Medico'
        context['listapac_url'] = reverse_lazy('medico_lista')
        context['action'] = 'editar'
        return context

class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = 'medico/eliminar_medico.html'
    success_url = reverse_lazy('medico_lista')

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
        context['title'] = 'Eliminar Medico'
        context['entidad'] = 'Medicos'
        context['listapac_url'] = reverse_lazy('medico_lista')

        return context
