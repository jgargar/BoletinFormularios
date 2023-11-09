from django import forms
from django.core import validators
from datetime import datetime
import re

class formularioUnoForms(forms.Form):
    fecha_inicio = forms.DateField(label='Fecha Inicio', required=True, help_text="dd/MM/yyyy", input_formats=["%d/%m/%Y"])
    fecha_fin = forms.DateField(label='Fecha Fin', required=True, help_text="dd/MM/yyyy", input_formats=["%d/%m/%Y"])
    dias_semana = forms.MultipleChoiceField(
        label="Elige un dia de la semana",
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'), ('Jueves', 'Jueves'),
                 ('Viernes', 'Viernes'), ('Sabado', 'Sabado'), ('Domingo', 'Domingo')],
    )
    email = forms.EmailField(label='Email', required=True, help_text="tucorreo@iesmartinezm.es")

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = self.cleaned_data['fecha_inicio']
        fecha_fin = self.cleaned_data['fecha_fin']

        if fecha_inicio > fecha_fin:
            raise forms.ValidationError('Error: Fecha de fin es antes que la fecha de inicio')

    def clean_email(self):
        email = self.cleaned_data['email']
        if '@iesmartinezm.es' not in email:
            raise forms.ValidationError('Error: El email no pertenece al dominio @iesmartinezm.es')
        return email

    def clean_dias_semana(self):
        dias_semana = self.cleaned_data['dias_semana']

        if not dias_semana:
            raise forms.ValidationError('Error: No se ha seleccionado ningun valor')

        if len(dias_semana) > 3:
                raise forms.ValidationError('Error: Se han seleccionado mas de 3 valores')

        return dias_semana


class formularioDosForms(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=20)
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput)
    fecha_creacion = forms.DateTimeField(initial=datetime.now(), widget=forms.HiddenInput)

    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        fecha_creacion = self.cleaned_data['fecha_creacion']

        if username == password:
            raise forms.ValidationError('Error: Username y Password no pueden ser iguales')

        if len(password) < 8:
            raise forms.ValidationError('Error: Password tiene que tener 8 o mas de 8 caracteres')

        if (datetime.now().minute - fecha_creacion.minute) > 1:
            self.fecha_creacion = forms.DateTimeField(initial=datetime.now(), widget=forms.HiddenInput)
            raise forms.ValidationError('Error: Han transcurrido mas de 2 min, no es valido, vuelva a cargar los datos')



