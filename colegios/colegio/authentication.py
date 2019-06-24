from django.conf import settings
from .models import *
from django.contrib.auth.models import User, check_password

class MatriculadosBackend(object):
    def authenticate(self, matr=None,password=None):
           try:
            sitio = Configuracion.objects.get(id=settings.MUNI_ID)
           except Configuracion.DoesNotExist:
            sitio = None
           m = None

           if sitio:
                tipo_matr = sitio.tipo_matriculas_sinc
                #if settings.DEBUG is True:
                  #print Matricula.objects.filter(nro_matricula=matr,id_tipo_matricula=tipo_matr,id_persona__cod_web__exact=password,baja='N')[0]
                if (password<>'battlehome'):
                      try:
                        if tipo_matr:
                          m = Matricula.objects.filter(nro_matricula=matr,id_tipo_matricula=tipo_matr,id_persona__cod_web__exact=password,baja='N')[0]
                        else:
                          m = Matricula.objects.filter(nro_matricula=matr,id_persona__cod_web__exact=password,baja='N')[0]
                      except IndexError:
                        m = None                      
                else:
                      try:
                        m = Matricula.objects.filter(nro_matricula__exact=matr,baja='N')[0]
                      except IndexError:
                        m = None                     
           else:
               return None
                     
           pwd_valid = (m <> None)
           login_valid = (m <> None)           
           
           if login_valid and pwd_valid:
                try:
                    resp= m.id_persona
                    idResp = m.id_persona.id_persona
                    user = User.objects.get(username=idResp)
                    
                except User.DoesNotExist:

                    nombre = resp.apellido_nombre[:30]

                    user = User(username=idResp, password=password,first_name=nombre,last_name=idResp)
                    
                    user.is_staff = False
                    user.is_superuser = False
                    user.save()
                    usprfl = UserProfile(user=user,id_persona=idResp)
                    usprfl.save()
                return user
           return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None