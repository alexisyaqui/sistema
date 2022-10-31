from django.db import models
from datetime import datetime
from django.forms import model_to_dict

# Create your models here.

class Nombre_Clinica(models.Model):
    nombre_clinica = models.CharField(max_length=50, verbose_name="Nombre de la Clinica", null=True, blank=True, )
    direccion_clinica = models.CharField(max_length=250, verbose_name="Direccion clinica", null=True, blank=True, )
    telefono_clinica = models.CharField(max_length=13, verbose_name="Numero de Telefono", null=True, blank=True, )
    nit_clinica = models.CharField(max_length=15, verbose_name="numero de nit clinica", null=True, blank=True, )
    mision = models.TextField(verbose_name="mision", null=True, blank=True, )
    vision = models.TextField(verbose_name="vision", null=True, blank=True, )

    # logo_clinica = models.ImageField(upload_to='media/Logo', verbose_name='logo clinica')

    def __str__(self):
        return self.nombre_clinica

    class Meta:
        verbose_name = 'Nombre Clinica'
        verbose_name_plural = 'Nombre Clinicas'
        ordering = ['id']


class Paciente(models.Model):
    class sexo(models.TextChoices):
        MASCULINO = 'M', 'Masculino',
        FEMENINO = 'F', 'Femenino'

    class religion(models.TextChoices):
        CATOLICO = 'CATOLICO', 'Catolico'
        EVANGELICO = 'EVANGELICO', 'Evangelico'
        MORMON = 'MORMON', 'Mormon'

    pnombre_pac = models.CharField(max_length=20, verbose_name='Nombre del paciente', null=True, blank=True, )
    snombre_pac = models.CharField(max_length=20, verbose_name='Segundo nombre del paciente', null=True, blank=True, )
    papellido_pac = models.CharField(max_length=20, verbose_name='Primer apellido paciente', null=True, blank=True, )
    sapellido_pac = models.CharField(max_length=50, verbose_name='Segundo apellido paciente', null=True, blank=True, )
    dpi_pac = models.CharField(max_length=15, verbose_name='Numero de DPI', null=True, blank=True, )
    fecha_nac_pac = models.DateField(verbose_name='fecha de nacimiento', null=True, blank=True, )
    direccion_pac = models.CharField(max_length=250, verbose_name='Direccion del Paciente', null=True, blank=True, )
    email_pac = models.EmailField(verbose_name='Direccion de correo electronico', null=True, blank=True, )
    telefono_pac = models.CharField(max_length=20, verbose_name='Numero de telefono paciente', null=True, blank=True, )
    sexo_pac = models.CharField(max_length=15, verbose_name='Sexo del Paciente', choices=sexo.choices)
    religion_pac = models.CharField(max_length=20, verbose_name='Religion', choices=religion.choices)

    def __str__(self):
        return self.pnombre_pac

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['id']


class Medico(models.Model):
    class sexo(models.TextChoices):
        MASCULINO = 'MASCULINO', 'Masculino',
        FEMENINO = 'FEMENINO', 'Femenino'

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class religion(models.TextChoices):
        CATOLICO = 'CATOLICO', 'Catolico'
        EVANGELICO = 'EVANGELICO', 'Evangelico'
        MORMON = 'MORMON', 'Mormon'

    pnombre_med = models.CharField(max_length=50, verbose_name='Nombre del Medico', null=False, blank=False, )
    snombre_med = models.CharField(max_length=50, verbose_name='Segundo nombre del Medico', null=True, blank=True, )
    papellido_med = models.CharField(max_length=50, verbose_name='Primer apellido Medico', null=True, blank=True, )
    sapellido_med = models.CharField(max_length=50, verbose_name='Segundo apellido Medico', null=True, blank=True, )
    dpi_med = models.CharField(max_length=15, verbose_name='Numero de DPI', null=True, blank=True, )
    fecha_nac_med = models.DateField(verbose_name='fecha de nacimiento', null=True, blank=True, )
    direccion_med = models.CharField(max_length=250, verbose_name='Direccion del Medico', null=True, blank=True, )
    email_med = models.EmailField(verbose_name='Direccion de correo electronico', null=True, blank=True, )
    titulo_medico = models.CharField(max_length=60, verbose_name="Titulo", null=True, blank=True, )
    colegiado_act = models.CharField(max_length=25, verbose_name='Colegiado Activo del Medico', null=True, blank=True, )
    telefono_med = models.IntegerField(verbose_name='Numero de telefono Medico', null=True, blank=True, )
    sexo_med = models.CharField(max_length=15, verbose_name='Sexo del Medico', choices=sexo.choices)
    religion_med = models.CharField(max_length=20, verbose_name='Religion', choices=religion.choices)

    def __str__(self):
        return self.pnombre_med
    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medico'

class Consulta(models.Model):
    motivo_consulta = models.CharField(max_length=250, verbose_name="Motivo de la Consulta")
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_consulta = models.DateTimeField()
    diagnostico = models.CharField(max_length=250, verbose_name="Diagnostico")
    observacion = models.TextField(verbose_name="Observacion")


    def __str__(self):
        return self.paciente.pnombre_pac + " " + self.medico.pnombre_med


    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['id']

