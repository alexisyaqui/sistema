# Generated by Django 4.1 on 2022-10-27 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_clinica', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consulta',
            options={'ordering': ['id'], 'verbose_name': 'Consulta', 'verbose_name_plural': 'Consultas'},
        ),
        migrations.AddField(
            model_name='medico',
            name='colegiado_act',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Colegiado Activo del Medico'),
        ),
    ]
