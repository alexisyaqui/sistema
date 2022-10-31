from django.forms import *
from app_clinica.models import *


class PacienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        # form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['pnombre_pac'].widget.attrs['autofocus'] = True

    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'pnombre_pac': TextInput(
                attrs={
                    'placeholder': 'Ingrese primer nombre',
                }
            ),
            'snombre_pac': TextInput(
                attrs={
                    'placeholder': 'Ingrese segundo nombre',
                }
            ),

            'papellido_pac': TextInput(
                attrs={
                    'placeholder': 'Ingrese primer apellido',
                }
            ),
            'sapellido_pac': TextInput(
                attrs={
                    'placeholder': 'Ingrese segundo apellido',
                }
            ),

            'dpi_pac': TextInput(
                attrs={
                    'placeholder': 'Ingrese numero de DPI',
                }
            ),

            'fecha_nac_pac': DateInput(
                attrs={
                    'placeholder': 'Ingrese fecha nacimiento',
                }
            ),
            'direccion_pac': TextInput(
                attrs={
                    'placeholder': 'Ingrese direccion domiciliar',
                }
            ),
            'email_pac': EmailInput(
                attrs={
                    'placeholder': 'Ingrese correo electronico',
                }
            ),
            'telefono_pac': TextInput(
                attrs={
                    'placeholder': 'Ingrese numero de telefono celular',
                }
            ),

            'sexo_pac': Select(
                attrs={
                    'placeholder': 'Ingrese genero',
                }
            ),
            'religion_pac': Select(
                attrs={
                    'placeholder': 'Ingrese religion',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    # def clean(self):
    #     cleaned = super().clean()
    #     if len(cleaned['pnombre_pac']) <= 50:
    #         raise forms.ValidationError('Validacion xxx')
    #         # self.add_error('name', 'Le faltan caracteres')
    #     return cleaned


class MedicoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pnombre_med'].widget.attrs['autofocus'] = True

    class Meta:
        model = Medico
        fields = '__all__'
        widgets = {
            'pnombre_med': TextInput(
                attrs={
                    'placeholder': 'Ingrese primer nombre',
                }
            ),
            'snombre_med': TextInput(
                attrs={
                    'placeholder': 'Ingrese segundo nombre',
                }
            ),

            'papellido_med': TextInput(
                attrs={
                    'placeholder': 'Ingrese primer apellido',
                }
            ),
            'sapellido_med': TextInput(
                attrs={
                    'placeholder': 'Ingrese segundo apellido',
                }
            ),

            'dpi_med': TextInput(
                attrs={
                    'placeholder': 'Ingrese numero de DPI',
                }
            ),

            'fecha_nac_med': DateInput(
                attrs={
                    'placeholder': 'Ingrese fecha nacimiento',
                }
            ),
            'direccion_med': TextInput(
                attrs={
                    'placeholder': 'Ingrese direccion domiciliar',
                }
            ),
            'email_med': EmailInput(
                attrs={
                    'placeholder': 'Ingrese correo electronico',
                }
            ),
            'titulo_medico': TextInput(
                attrs={
                    'placeholder': 'Ingrese titulo',
                }
            ),
            'colegiado_act': TextInput(
                attrs={
                    'placeholder': 'Ingrese Colegiado activo del Medico',
                }
            ),
            'telefono_med': TextInput(
                attrs={
                    'placeholder': 'Ingrese numero de telefono celular',
                }
            ),

            'sexo_med': Select(
                attrs={
                    'placeholder': 'Ingrese genero',
                }
            ),
            'religion_med': Select(
                attrs={
                    'placeholder': 'Ingrese religion',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    # def clean(self):
    #     cleaned = super().clean()
    #     if len(cleaned['pnombre_pac']) <= 50:
    #         raise forms.ValidationError('Validacion xxx')
    #         # self.add_error('name', 'Le faltan caracteres')
    #     return cleaned


class ConsultaMedicaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['motivo_consulta'].widget.attrs['autofocus'] = True

    class Meta:
        model = Consulta
        fields = '__all__'
        widgets = {
            'motivo_consulta': TextInput(
                attrs={
                    'placeholder': 'Ingrese motivo de su consulta',
                }
            ),
            'persona': Select(
                attrs={
                    'placeholder': 'Seleccione el paciente',
                }
            ),
            'medico': Select(
                attrs={
                    'placeholder': 'Seleccione el Medico',
                }
            ),

            'diagnostico': Textarea(
                attrs={
                    'placeholder': 'Ingrese el diagnostico del paciente',
                }
            ),
            'fecha_consulta': DateInput(
                attrs={
                    'placeholder': 'Ingrese de la consulta',
                }
            ),

            'observacion': Textarea(
                attrs={
                    'placeholder': 'Observaciones y recomendaciones del paciente',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    # def clean(self):
    #     cleaned = super().clean()
    #     if len(cleaned['pnombre_pac']) <= 50:
    #         raise forms.ValidationError('Validacion xxx')
    #         # self.add_error('name', 'Le faltan caracteres')
    #     return cleaned
