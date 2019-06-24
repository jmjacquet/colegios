# -*- coding: utf-8 -*-
from django import forms
from .models import *
from django.forms import ModelForm
from django.forms.models import BaseInlineFormSet
import datetime
from .utilidades import MESES,ANIOS
from django.contrib import admin

from django.forms.widgets import TextInput,NumberInput



CHOICES = (('0', 'Documentación',),)

class UploadForm(forms.Form):
      
    destino = forms.ChoiceField(choices=CHOICES,label='Seleccione el Tipo de Archivo')
    archivo = forms.FileField(
        label='Seleccione un archivo'
    )
    def clean(self):
        archivo = self.cleaned_data.get('archivo')
        # 5MB - 5242880
        if archivo:
            if archivo._size > 2097152:            
                self._errors["archivo"] = [u"El archivo no debe superar los 2048KB! (2MB)"]  

class IngresoForm(forms.Form):         
    usuario = forms.IntegerField(max_value=999999999,min_value=0,label='Usuario') 
    password = forms.CharField(max_length=50)
    def clean(self):
        super(forms.Form,self).clean()
        try:
            ndoc=self.cleaned_data['ndoc'] 
        except:
            self._errors['ndoc'] = [u'Debe cargar al menos 6 dígitos del Documento.']
            return self.cleaned_data
        
        if (ndoc<=99999):
                self._errors['ndoc'] = [u'Debe cargar al menos 6 dígitos del Documento.']        

        return self.cleaned_data



class OS_DetallesAdmin(admin.ModelAdmin):
    list_display = ('id_os','tipo','link','det_codigo','det_detalle','det_col1','det_col2')
    search_fields = ['id_os__detalle','det_codigo']

admin.site.register(Persona) 
admin.site.register(Matricula)
admin.site.register(Cuota)
admin.site.register(CuotaDetalle)

admin.site.register(ObraSocial)
admin.site.register(OS_Detalles,OS_DetallesAdmin)