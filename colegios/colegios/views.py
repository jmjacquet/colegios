# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth import logout as django_logout
from django.shortcuts import *
from settings import *
from django.core.urlresolvers import reverse
from django.contrib import messages
from colegio.models import *
from django.db.models import Q

LOGIN_REDIRECT_URL='/'

def login(request):
    error = None
    LOGIN_REDIRECT_URL='/'    

    if request.user.is_authenticated():
      LOGIN_REDIRECT_URL=reverse('principal')
      return HttpResponseRedirect(LOGIN_REDIRECT_URL)
      
    try:
        sitio = Configuracion.objects.get(id=MUNI_ID)
    except Configuracion.DoesNotExist:
        sitio = None
    try:
    	if(sitio.mantenimiento == 1):
        	return render_to_response('mantenimiento.html', {'dirMuni':MUNI_DIR,'sitio':sitio},context_instance=RequestContext(request))
    except:
    	sitio.mantenimiento = 0
    	sitio.save()
          

    if request.method == 'POST':        
        user = authenticate(matr=request.POST['matr'],password=request.POST['password'])      
        if user is not None:
          if user.is_active:
            django_login(request, user)
            request.session["usuario"] = request.user.username               
            LOGIN_REDIRECT_URL = '/cuotas/'+str(request.user.userprofile.id_persona)
            return HttpResponseRedirect(LOGIN_REDIRECT_URL)
          else:
          ## invalid login
           error = u"Matrícula/Código incorrectos."
        else:
          ## invalid login
           error = u"Matrícula/Código incorrectos."
          #return direct_to_template(request, 'invalid_login.html')
    if error:
      messages.add_message(request, messages.ERROR,u'%s' % (error))    

    template = 'index.html'      
   
    return render_to_response(template, {'dirMuni':MUNI_DIR,'sitio':sitio},context_instance=RequestContext(request))

def salir(request):
    request.session.clear()
    django_logout(request)
    return HttpResponseRedirect(LOGIN_REDIRECT_URL)

def volverHome(request):
    LOGIN_REDIRECT_URL='/'
    if not request.user.is_authenticated():
      return HttpResponseRedirect(LOGIN_URL)
    try:
        LOGIN_REDIRECT_URL = reverse('principal')
    except:
      return HttpResponseRedirect(LOGIN_URL)    
    return HttpResponseRedirect(LOGIN_REDIRECT_URL)



