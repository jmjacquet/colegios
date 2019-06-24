# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from .utilidades import TIPO_DOC,PROVINCIAS,ESTADO,TIPO_DETALLE_OS
from django.contrib.auth.models import User
from datetime import datetime,date
from dateutil.relativedelta import *
from django.conf import settings
import os 

class Persona(models.Model):
    id_persona = models.IntegerField(db_column='ID_PERSONA',primary_key=True) # Field name made lowercase.
    tipo_doc = models.IntegerField(db_column='ID_TIPO_DOC',choices=TIPO_DOC,default=3 ,blank=True, null=True) # Field name made lowercase.
    id_pais = models.IntegerField(db_column='ID_PAIS', blank=True, null=True) # Field name made lowercase.
    id_estado_civil = models.IntegerField(db_column='ID_ESTADO_CIVIL', blank=True, null=True) # Field name made lowercase.
    codigo_persona = models.CharField(db_column='CODIGO_PERSONA', max_length=10, blank=True, null=True) # Field name made lowercase.
    apellido_nombre = models.CharField(db_column='APELLIDO_NOMBRE', max_length=100,blank=True, null=True) # Field name made lowercase.
    nro_documento = models.CharField(db_column='NRO_DOCUMENTO', max_length=20, blank=True, null=True) # Field name made lowercase.
    fecha_nac = models.DateField(db_column='FECHA_NAC', blank=True, null=True) # Field name made lowercase.
    sexo = models.CharField(db_column='SEXO', max_length=1, blank=True, null=True) # Field name made lowercase.
    cuit_cuil = models.CharField(db_column='CUIT_CUIL', max_length=30, blank=True, null=True) # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO', max_length=100, blank=True, null=True) # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True) # Field name made lowercase.
    cod_web = models.CharField(db_column='COD_WEB', max_length=10, blank=True, null=True) # Field name made lowercase.
    baja = models.CharField(db_column='BAJA', max_length=1, blank=True, null=True) # Field name made lowercase.
    domlegal_calle = models.CharField(db_column='DOMLEGAL_CALLE', max_length=100, blank=True, null=True) # Field name made lowercase.
    domlegal_piso = models.CharField(db_column='DOMLEGAL_PISO', max_length=50, blank=True, null=True) # Field name made lowercase.
    domlegal_dpto = models.CharField(db_column='DOMLEGAL_DPTO', max_length=50, blank=True, null=True) # Field name made lowercase.
    domlegal_nro = models.CharField(db_column='DOMLEGAL_NRO', max_length=50, blank=True, null=True) # Field name made lowercase.
    domlegal_localidad = models.CharField(db_column='DOMLEGAL_LOCALIDAD', max_length=100, blank=True, null=True) # Field name made lowercase.
    domlegal_telefono = models.CharField(db_column='DOMLEGAL_TELEFONO', max_length=100, blank=True, null=True) # Field name made lowercase.
    domlegal_codpostal = models.CharField(db_column='DOMLEGAL_CODPOSTAL', max_length=50, blank=True, null=True) # Field name made lowercase.
    domlegal_id_provincia = models.IntegerField(db_column='DOMLEGAL_ID_PROVINCIA', blank=True, null=True,choices=PROVINCIAS, default='21') # Field name made lowercase.
    domreal_calle = models.CharField(db_column='DOMREAL_CALLE', max_length=100, blank=True, null=True) # Field name made lowercase.
    domreal_piso = models.CharField(db_column='DOMREAL_PISO', max_length=50, blank=True, null=True) # Field name made lowercase.
    domreal_dpto = models.CharField(db_column='DOMREAL_DPTO', max_length=50, blank=True, null=True) # Field name made lowercase.
    domreal_nro = models.CharField(db_column='DOMREAL_NRO', max_length=50, blank=True, null=True) # Field name made lowercase.
    domreal_localidad = models.CharField(db_column='DOMREAL_LOCALIDAD', max_length=100, blank=True, null=True) # Field name made lowercase.
    domreal_telefono = models.CharField(db_column='DOMREAL_TELEFONO', max_length=100, blank=True, null=True) # Field name made lowercase.
    domreal_codpostal = models.CharField(db_column='DOMREAL_CODPOSTAL', max_length=50, blank=True, null=True) # Field name made lowercase.
    domreal_id_provincia = models.IntegerField(db_column='DOMREAL_ID_PROVINCIA', blank=True, null=True,choices=PROVINCIAS, default='21')  # Field name made lowercase.
    class Meta:
        db_table = 'persona'
        verbose_name_plural = u'Personas'  

    def __unicode__(self):
        return u'%s' % (self.apellido_nombre)



class Matricula(models.Model):
    id_matricula = models.IntegerField(primary_key=True)
    id_persona = models.ForeignKey('Persona',db_column='id_persona',db_index=True)
    nro_matricula = models.CharField(max_length=50,blank=True, null=True)
    fecha_titulo = models.DateField(blank=True, null=True)
    fecha_alta = models.DateField(blank=True, null=True)
    detalle = models.CharField(max_length=500,blank=True, null=True)
    baja = models.CharField(max_length=1, blank=True, null=True) # Field name made lowercase.
    fecha_baja = models.DateField(blank=True, null=True) 
    tipo_matricula = models.CharField(max_length=50, blank=True, null=True) # Field name made lowercase.
    id_tipo_matricula = models.IntegerField(blank=True, null=True) # Field name made lowercase.
    folio =models.CharField(max_length=10, blank=True, null=True) # Field name made lowercase.
    libro = models.CharField(max_length=10, blank=True, null=True) # Field name made lowercase.
    fecha_finalizacion = models.DateField(blank=True, null=True) 
    nro_superintendencia = models.CharField(max_length=50, blank=True, null=True) # Field name made lowercase.
    universidad = models.CharField(max_length=100, blank=True, null=True) # Field name made lowercase.
    titulo = models.CharField(max_length=100, blank=True, null=True) # Field name made lowercase.
    facultad = models.CharField(max_length=100, blank=True, null=True) # Field name made lowercase.
    class Meta:        
        db_table = 'matricula'
        verbose_name_plural = u'Matriculas'  

    def __unicode__(self):
        return u'%s' % (self.nro_matricula)

class Tributo(models.Model):
    id_tributo = models.IntegerField(primary_key=True,null=False)
    descripcion = models.CharField(max_length=200, blank=True)    
    tipo_interes = models.IntegerField(blank=True, null=True) # Field name made lowercase.
    interes_especial = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True) # Field name made lowercase.
    baja = models.CharField(max_length=1, blank=True, null=True) # Field name made lowercase.
    class Meta:
        db_table = 'tributo'

    def __unicode__(self):
        return u'%s' % (self.descripcion)


class Cuota(models.Model):
    id_cuota = models.IntegerField(primary_key=True)
    id_generacion = models.IntegerField(blank=True, null=True)    
    id_persona = models.ForeignKey('Persona',db_column='id_persona',db_index=True)
    id_estado = models.IntegerField(blank=True, null=True,choices=ESTADO, default='21')
    id_matricula = models.ForeignKey('Matricula',db_column='id_matricula',db_index=True)
    anio = models.IntegerField(blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True)
    importe_base = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    importe_base_2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fecha_vencim = models.DateField()
    fecha_vencim_2 = models.DateField()
    saldo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)    
    detalle = models.CharField(max_length=500,blank=True, null=True)
    id_tributo = models.ForeignKey('Tributo',db_column='id_tributo',db_index=True)
    class Meta:        
        db_table = 'cuotas_web'
        verbose_name_plural = u'Cuotas'  

    def __unicode__(self):
        return u'%s' % (self.id_cuota)

class CuotaDetalle(models.Model):
    id_cuota_detalle = models.IntegerField(db_column='ID_CUOTA_DETALLE', primary_key=True) # Field name made lowercase.
    id_cuota = models.ForeignKey('Cuota', db_column='ID_CUOTA',blank=True, null=True)
    id_concepto = models.IntegerField(db_column='ID_CONCEPTO',db_index=True,blank=True, null=True)
    id_pago = models.IntegerField(db_column='ID_PAGO', blank=True, null=True) # Field name made lowercase.
    detalle = models.CharField(db_column='DETALLE', max_length=500, blank=True, null=True) # Field name made lowercase.
    detalle_descuento = models.CharField(db_column='DETALLE_DESCUENTO', max_length=500, blank=True, null=True) # Field name made lowercase.
    importe_base = models.DecimalField(db_column='IMPORTE_BASE', max_digits=15, decimal_places=2, blank=True, null=True) # Field name made lowercase.    
    debito_credito = models.IntegerField(db_column='DEBITO_CREDITO', blank=True, null=True) # Field name made lowercase.    
    aud_fecha = models.DateField(db_column='AUD_FECHA', blank=True, null=True) # Field name made lowercase.
    aud_usuario = models.CharField(db_column='AUD_USUARIO', max_length=20,blank=True, null=True) # Field name made lowercase.    
    orden = models.IntegerField(db_column='ORDEN', blank=True, null=True) # Field name made lowercase.
    class Meta:
        db_table = 'cuota_detalle'
        verbose_name_plural = u'Detalle Cuotas'  


#Tabla de la Base de Configuracion
class Configuracion(models.Model):
    id = models.IntegerField(primary_key=True,db_index=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)   
    punitorios = models.DecimalField(max_digits=15, decimal_places=4,null=True)
    tipo_punitorios = models.IntegerField(null=True)
    linea1 = models.CharField(max_length=100, blank=True,null=True)
    linea2 = models.CharField(max_length=100, blank=True,null=True)
    link_retorno = models.CharField(max_length=100, blank=True,null=True)
    mantenimiento = models.IntegerField(blank=True,null=True)
    codigo_visible = models.CharField(max_length=1, blank=True,null=True)
    diasextravencim = models.IntegerField(db_column='diasExtraVencim', blank=True, null=True) # Field name made lowercase.    
    liquidacion_web = models.CharField(max_length=1, blank=True,default='S',null=True)
    email = models.CharField(max_length=50, blank=True,null=True) # Field name made lowercase.
    tipo_matriculas_sinc = models.IntegerField(blank=True,null=True)
    cod_entidad_codbar = models.IntegerField(blank=True,null=True)
    #tipoLogin = models.IntegerField(choices=TIPO_LOGIN,default=0)
    class Meta:
        db_table = 'configuracion'
    
    def __unicode__(self):
        return u'%s' % (self.nombre)

#Tabla de Usuario con datos Extra
class UserProfile(models.Model):
    id_persona = models.IntegerField(blank=True, null=True)
    user = models.OneToOneField(User)

    class Meta:
        db_table = 'user_profile'

    def __unicode__(self):
        return self.user.username        


class Sinc(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(db_index=True)
    hora = models.TimeField()
    ultimo_id = models.IntegerField()
    class Meta:
        db_table = 'sinc'
        managed = False


class ObraSocial(models.Model):
    id_os = models.AutoField(db_column='ID_OS', primary_key=True) # Field name made lowercase.  
    detalle = models.CharField(db_column='DETALLE', max_length=500, blank=True,null=True) # Field name made lowercase.    
    class Meta:
        db_table = 'obra_social'
        verbose_name_plural = u'Obras Sociales'  

    def __unicode__(self):
        return self.detalle

class OS_Detalles(models.Model):
    id_os = models.ForeignKey('ObraSocial', db_column='ID_OS')    
    tipo = models.IntegerField(blank=True, null=True,choices=TIPO_DETALLE_OS, default='1')
    link = models.CharField(db_column='link', max_length=500, blank=True,null=True) # Field name made lowercase.    
    det_codigo = models.CharField(db_column='codigo', max_length=50, blank=True,null=True) # Field name made lowercase.    
    det_detalle = models.CharField(db_column='detalle', max_length=500, blank=True,null=True) # Field name made lowercase.    
    det_col1 = models.CharField(db_column='col1', max_length=50, blank=True,null=True) # Field name made lowercase.    
    det_col2 = models.CharField(db_column='col2', max_length=50, blank=True,null=True) # Field name made lowercase.    
    class Meta:
        db_table = 'os_detalle'        
        verbose_name_plural = u'Detalle Obras Sociales'  

    def __unicode__(self):
        return u'%s %s %s ' % (self.link,self.det_codigo,self.det_detalle)



class ArchivosDoc(models.Model):
    archivo = models.FileField(max_length=1000,upload_to=os.path.join(settings.MEDIA_ROOT,os.path.join('Documentos',settings.MUNI_DIR)))
        