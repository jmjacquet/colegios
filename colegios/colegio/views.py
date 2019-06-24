# -*- coding: utf-8 -*-
from django.template import RequestContext,Context
from django.shortcuts import *
from .models import *
from django.views.generic import TemplateView,ListView,CreateView,UpdateView
from django.conf import settings
from django.db.models import Count,Sum
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db import connection
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response,redirect
from django.contrib import messages
from .utilidades import *
from django import http
import os 
try:
    import json
except ImportError:
    from django.utils import simplejson as json

from datetime import datetime,date,timedelta
from django.utils import timezone
from dateutil.relativedelta import *
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


def puedeVerPadron(request,idPersona):
    usr=request.user    
    if not (int(idPersona)==int(usr.userprofile.id_persona)):
        print 'NO TIENE PERMISO!'
        raise http.Http404


##############################################
#      Mixin para cargar las Vars de sistema #
##############################################

class VariablesMixin(object):
    def get_context_data(self, **kwargs):
        context = super(VariablesMixin, self).get_context_data(**kwargs)
        context['idMuni'] = settings.MUNI_ID
        context['dirMuni'] = settings.MUNI_DIR

        # try:
        #     sinc = Sinc.objects.all().order_by('-fecha','-hora')[0]
        # except Sinc.DoesNotExist:
        #     sinc = None
        try:
            sitio = Configuracion.objects.get(id=settings.MUNI_ID)
        except Configuracion.DoesNotExist:
            sitio = None
        
        try:
            idPersona= int(self.request.user.userprofile.id_persona)                
            context['persona'] = Persona.objects.get(id_persona=idPersona)           
            context['matricula'] = Matricula.objects.filter(id_persona__id_persona=idPersona)[0]
        except:
            context['persona'] = None
            context['matricula'] = None
        
        context['sitio'] = sitio
        #context['sinc'] = sinc
        return context

    
class PrincipalView(VariablesMixin,TemplateView):
    template_name = 'datos_matricula.html'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
         return super(PrincipalView, self).dispatch(*args, **kwargs)
   

##################################################
#      Ver cuotas del Matriculado seleccionado        #
##################################################

class BusquedaCuotasView(VariablesMixin,ListView):
    template_name = 'cuotas.html'
    context_object_name = 'cuotas'
 
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        idPersona = self.kwargs.get("idp",'0')        
        puedeVerPadron(self.request,idPersona)
        return super(BusquedaCuotasView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        # Tomo la persona y anio seleccionado y lo filtro para que me muestre las cuotas
        idPersona = self.kwargs.get("idp",'0')                
        anio = int(self.kwargs.get("anio",'0'))

        if (anio==0):
            c = Cuota.objects.filter(id_persona=idPersona).order_by('-fecha_vencim')
        else:
            c = Cuota.objects.filter(id_persona=idPersona,anio=anio).order_by('-fecha_vencim')
        return c

    def get_context_data(self, **kwargs):
        context = super(BusquedaCuotasView, self).get_context_data(**kwargs)
        # En el contrxto pongo el padrón seleccionado asi saco sus características
        idPersona = self.kwargs.get("idp",'0')                
        anio = int(self.kwargs.get("anio",'0'))
        context['anio']=anio                
        return context

##########################################################################3        

class ObrasSocialesView(VariablesMixin,TemplateView):
    template_name = 'obrasociales.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ObrasSocialesView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ObrasSocialesView, self).get_context_data(**kwargs)
        detalles_oss=OS_Detalles.objects.all()      
        id_oss = detalles_oss.values_list('id_os', flat=True).distinct()   
        oss = ObraSocial.objects.filter(pk__in=id_oss)
        context['oss'] = oss
        context['detalles_oss'] = detalles_oss
       
        return context

##########################################
#        Datos Adicionales        #
##########################################

class TerminosyCondicView(VariablesMixin,TemplateView):
    template_name = 'terminosCondic.html'

class DocumentacionView(VariablesMixin,TemplateView):
    template_name = 'documentos.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DocumentacionView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DocumentacionView, self).get_context_data(**kwargs)
        idPersona= int(self.request.user.userprofile.id_persona)               

        #file_path = os.path.join(settings.MEDIA_ROOT, 'Documentos')
        file_path = os.path.join(settings.MEDIA_ROOT,os.path.join('Documentos',settings.MUNI_DIR))
        file_list = [entry for entry in os.listdir(file_path) if os.path.isfile(os.path.join(file_path,entry))]
        nombres = [os.path.splitext(x)[0] for x in file_list]
        dicc = dict(zip(file_list, nombres))
       
        context['dicc'] = sorted(dicc.iteritems())
       
        return context


def armarCodBar(cod):
    import imprimirPDF
    b  = imprimirPDF.get_image2(cod)
    return b

def imprimirPDF(request,idc):   
    
    from Code128 import Code128
    from base64 import b64encode
        
    c = Cuota.objects.get(id_cuota=idc)    
    #puedeVerPadron(request,c.id_unidad.pk)

    diasExtra = None
    try:
        sitio = Configuracion.objects.get(id=settings.MUNI_ID)
        diasExtra = sitio.diasextravencim

    except Configuracion.DoesNotExist:
        sitio = None
        
    if diasExtra == None:
        diasExtra=0

    hoy = date.today()

    if (hoy >= c.fecha_vencim):
        vencimiento = hoy + relativedelta(days=diasExtra)   
        vencimiento2 = vencimiento
    else:
        vencimiento = c.fecha_vencim
        if c.fecha_vencim_2==None:
           vencimiento2 = vencimiento + relativedelta(months=1)
        else:
            vencimiento2 = c.fecha_vencim_2   
    
    detalle_cuotas = CuotaDetalle.objects.filter(id_cuota__pk=idc)

    context = Context()    
    context['cuota'] = c
    context['idMuni'] = settings.MUNI_ID
    context['dirMuni'] = settings.MUNI_DIR
    context['sitio'] = sitio

    context['fecha'] = datetime.now()
    context['vencimiento'] = vencimiento
    context['codseg'] = c.id_persona.cod_web
    context['sitio'] = sitio
    context['detalle_cuotas'] = detalle_cuotas
    
    from easy_pdf.rendering import render_to_pdf_response   
 
    template = 'boletas/boleta.html'
    totales  = calcularPunitorios(request,c,None,0)
    context['vencimiento2'] = vencimiento2
    
    context['cod_pagos'] = str(c.id_matricula.id_matricula).rjust(9, "0")
    context['punit1'] = totales['punit1']
    context['interes1'] = totales['porc1']
    context['punit2'] = totales['punit2']
    context['interes2'] = totales['porc2']

    sAnio=str(c.anio)
    sAnio=sAnio[-2:] #Dos ultimos digitos del anio
    if c.id_tributo is None:
        tributo = 1
    else:
        tributo=c.id_tributo.id_tributo
    cod = ""
    cod += str(sitio.cod_entidad_codbar).rjust(3, "0") #CODIGO DEL MUNICIPIO
    cod += str(tributo).rjust(1, "0") #TRIBUTO
    cod += str(c.id_matricula.id_matricula).rjust(6, "0") #Matricula
    cod += sAnio #Anio
    cod += str(c.periodo).rjust(2, "0") #Cuota    
    cod += str(c.id_cuota).rjust(7, "0") #Id Cuota
    cod += str(vencimiento.strftime("%d%m%y")).rjust(6, "0") #Vencimiento
    cod += str(totales['punit1']).replace(".","").rjust(7, "0") #Importe Actualizado
    cod += str(vencimiento2.strftime("%d%m%y")).rjust(6, "0") #Vencimiento2
    cod += str(totales['punit2']).replace(".","").rjust(7, "0") #Importe2 Actualizado
    
    cod += str(digVerificador(cod))
    
    path = 'staticfiles/localidad/'+settings.MUNI_DIR+'/'
    
    context['codbar'] = armarCodBar(cod)
    context['codigo'] = cod
    
    return render_to_pdf_response(request, template, context)    



####################################################
 
def calcularPunitorios(request,c,boleta=None,importe=0):
    try:
        cuota = c       
        hoy = date.today()  
        vencimiento = cuota.fecha_vencim

        if cuota.fecha_vencim_2==None:
           vencimiento2 = vencimiento + relativedelta(months=1)
        else:
            vencimiento2 = cuota.fecha_vencim_2           

        fecha = hoy  

  
        if (hoy<=vencimiento):
            fecha=vencimiento                          
        elif ((hoy>vencimiento)and(hoy<=vencimiento2)):
            fecha=vencimiento2
        else:
            fecha=hoy
            vencimiento2=fecha
            
        por1 = punitorios(cuota,vencimiento,fecha)
        por2 = punitorios(cuota,vencimiento,vencimiento2)
        punit1 = cuota.saldo * (1+por1) 
        porc1 = punit1 - cuota.saldo
        punit2 = cuota.saldo * (1+por2)
        porc2 =  punit2 - cuota.saldo       
    except KeyError:
        return HttpResponse('Error') # Error Manejado
    if settings.DEBUG:
        print 'por1:'+str(por1)+' porc1:'+str(porc1)+' punit1:'+str(punit1)+' por2:'+str(por2)+' porc2:'+str(porc2)+' punit2:'+str(punit2)
    return {'punit1': format(punit1, '.2f'), 'porc1': format(porc1, '.2f'),'punit2': format(punit2, '.2f'), 'porc2': format(porc2, '.2f')}



##################################################################

from .forms import UploadForm
from django.utils.text import slugify

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']
            destino = request.POST['destino']            
            archivo.name = archivo.name.replace(" ", "_").replace("-", "_")
            print archivo.name
            fileName = archivo.name.replace(" ", "_")
            if destino=='0':        
                newdoc = ArchivosDoc(archivo = archivo)    
            else:
                newdoc = ArchivosDoc(archivo = archivo)            
            newdoc.save()
            return redirect("/datos/")
    else:
        form = UploadForm()
    return render_to_response('subirArchivos.html', {'form': form}, context_instance = RequestContext(request))

@login_required
def delete_file(request,fileName):    
    file_path = os.path.join(settings.MEDIA_ROOT,os.path.join('Documentos',settings.MUNI_DIR))    
    os.remove(os.path.join(file_path,fileName))
    try:
        archivo = ArchivosDoc.objects.get(archivo=fileName)
        archivo.delete()
    except:
        return redirect("/datos/")

    return redirect("/datos/")


#####################################################################

class MatriculadosView(VariablesMixin,TemplateView):
    template_name = 'matriculados.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MatriculadosView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MatriculadosView, self).get_context_data(**kwargs)
        matriculados=Matricula.objects.exclude(id_matricula=0).select_related('id_persona')
        
        context['matriculados'] = matriculados        
       
        return context