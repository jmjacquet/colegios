# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import decimal
from django.contrib import messages
from django.conf import settings
from django.contrib.messages import constants as message_constants

MESSAGE_TAGS = {message_constants.DEBUG: 'debug',
                message_constants.INFO: 'info',
                message_constants.SUCCESS: 'success',
                message_constants.WARNING: 'warning',
                message_constants.ERROR: 'danger',}

TIPO_LOGIN = (    
    (0, 'Barrio/Lote/Manzana'),
    (1, 'Usuario/Contrasenia')
)

TIPO_DOC = (    
    (1, 'LE'),
    (2, 'LC'),
    (3, 'DNI'),
    (4, 'CEDULA'),
    (5, 'CUIL'),
)

ESTADO = (    
    (1, 'NORMAL'),
    (2, 'PAGADA')
)


TIPO_DETALLE_OS = (    
    (1, 'LINK_ARCHIVO'),
    (2, 'FILA'),
    (3, 'TEXTO'),
    (4, 'LINK_WEB'),
)


ANIOS = (
	('2018', '2018'),
    ('2017', '2017'),
    ('2016', '2016'),
    ('2015', '2015'),
    ('2014', '2014'),
    ('2013', '2013'),
    ('2012', '2012'),
    ('2011', '2011'),
    ('2010', '2010'),
)

MESES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
)

PERIODOS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
)

PROVINCIAS = (
(1, 'BUENOS AIRES'),          
(2, 'CAPITAL FEDERAL'),       
(3, 'CATAMARCA'),             
(4, 'CHACO'),                 
(5, 'CHUBUT'),                
(6, 'CORDOBA'),               
(7, 'CORRIENTES'),            
(8, 'ENTRE RIOS'),            
(9, 'FORMOSA'),               
(10, 'JUJUY'),                
(11, 'LA PAMPA'),             
(12, 'LA RIOJA'),             
(13, 'MENDOZA'),              
(14, 'MISIONES'),             
(15, 'NEUQUEN'),              
(16, 'RIO NEGRO'),            
(17, 'SALTA'),                
(18, 'SAN JUAN'),             
(19, 'SAN LUIS'),             
(20, 'SANTA CRUZ'),           
(21, 'SANTA FE'),             
(22, 'SANTIAGO DEL ESTERO'),  
(23, 'TIERRA DEL FUEGO'),     
(24, 'TUCUMAN'),  
)            

def digVerificador(num):
    lista = list(num)
    pares= lista[1::2]
    impares= lista[0::2]
    
    totPares = 0
    totImpares = 0

    for i in pares:
        totPares=totPares+int(i*3)

    for i in impares:
        totImpares=totImpares+int(i)
 
    final = totImpares+totPares

    while (final > 9):
        cad=str(final)
        tot=0
        for i in cad:
            tot=tot+int(i)
        final=tot

    return final


def punitorios(cuota,vencimiento,fecha_punit):
    from .models import Configuracion
    porc = 0
    tipo_interes = cuota.id_tributo.tipo_interes
    interes = cuota.id_tributo.interes_especial
    
    try:      
        fecha_punit = fecha_punit
        tipo_interes = cuota.id_tributo.tipo_interes
        interes = cuota.id_tributo.interes_especial
        dias=0
        meses=0

        #Si no tiene definido el interés, lo busco en la configuración
        if interes == None:           
           interes = Configuracion.objects.get(id=settings.MUNI_ID).punitorios
           
        if tipo_interes == None:            
           tipo_interes = Configuracion.objects.get(id=settings.MUNI_ID).tipo_punitorios


        if tipo_interes == None:
           tipo_interes = 1 
        
        if interes == None:
           interes = 0 
        
        #DIARIO
        if tipo_interes == 2:
            try:
                dias = (fecha_punit - vencimiento).days
            except:
                dias = 0
            if dias < 0:
                dias = 0 
            porc =  (interes/30) * dias
            
        #MENSUAL
        elif tipo_interes == 1:
            try:
                meses = (fecha_punit - vencimiento).days / 30
            except:
                meses = 0
            if meses < 0:
                meses = 0 
            porc =  (interes * meses)        
        else:
            try:
                dias = (fecha_punit - vencimiento).days
            except:
                dias = 0
            if dias < 0:
                dias = 0 
            porc =  (interes / 30 ) * dias

        if porc < 0:
            porc = 0
        
        if settings.DEBUG:
            print 'Interes:'+str(interes)+' TipoInteres:'+str(tipo_interes)+' Meses:'+str(meses)+' Dias:'+str(dias)+' Porc: '+str(porc)+' Venc: '+str(vencimiento)+' FechaPunit: '+str(fecha_punit)
    except KeyError:
        return HttpResponse('Error') # incorrect post
    return porc