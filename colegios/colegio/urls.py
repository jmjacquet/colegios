# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.conf import settings
import os
from views import *
from django.views.generic import RedirectView,TemplateView

urlpatterns = patterns('boletas.views',
	
    # url(r'^estudios/$', EstudiosView.as_view(),name="padrones_estudio"),
    
    # url(r'^$', PrincipalView.as_view(),name="principal"),
    url(r'^principal/$', PrincipalView.as_view(),name="principal"),
    url(r'^cuotas/$', BusquedaCuotasView.as_view(),name="ver_cuotas"),
    url(r'^cuotas/(?P<idp>[^/]+)/$', BusquedaCuotasView.as_view(),name="ver_cuotas"),
    url(r'^cuotas/(?P<idp>[^/]+)/(?P<anio>\d+)/$', BusquedaCuotasView.as_view(),name="buscarCuotasAP"),
    # url(r'^punitorios/(?P<idc>\d+)/$',calcularPunitoriosForm,name="calcularPunitorios"),
    # url(r'^punitoriosLiq/(?P<idp>\d+)/$',generarPunitoriosLiq,name="generarPunitoriosLiq"),
    url(r'^imprimir/(?P<idc>\d+)/$',imprimirPDF,name="imprimirPDF"),
    url(r'^datos/$', DocumentacionView.as_view(),name="datos"),
    url(r'^oss/$', ObrasSocialesView.as_view(),name="obras_sociales"),
    url(r'^terminos/$', TerminosyCondicView.as_view(),name="terminos"),
    url(r'^matriculados/$', MatriculadosView.as_view(),name="matriculados"),  
    url(r'^uploads/', upload_file, name="subirArchivos"),
    url(r'^delete/Documentos/'+settings.MUNI_DIR+'/(?P<fileName>[\w.]{0,256})$', delete_file, name="delete_file"),
    #url(r'^delete/ejecutado_expensas/(?P<fileName>[\w.]{0,256})$', delete_file2, name="delete_file2"),
    )