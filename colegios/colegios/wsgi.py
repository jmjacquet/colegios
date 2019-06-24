
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))

sys.path.append(PROJECT_DIR)


# os.environ['DJANGO_SETTINGS_MODULE'] = 'colegios.settings'
# os.environ['MUNI_ID'] = environ['MUNI_ID']
# os.environ['MUNI_DB'] = environ['MUNI_DB']
# os.environ['MUNI_DIR'] = environ['MUNI_DIR']

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
from django.core.handlers.wsgi import WSGIHandler
import django
import os

class WSGIEnvironment(WSGIHandler):

    def __call__(self, environ, start_response):

    	os.environ['MUNI_ID'] = environ['MUNI_ID']
    	os.environ['MUNI_DB'] = environ['MUNI_DB']
    	os.environ['MUNI_DIR'] = environ['MUNI_DIR']
    	os.environ['DJANGO_SETTINGS_MODULE'] = 'colegios.settings'
    	django.setup()
    	return super(WSGIEnvironment, self).__call__(environ, start_response)

application = WSGIEnvironment()

# def application(environ, start_response):
#   os.environ['MUNI_ID'] = environ['MUNI_ID']
#   os.environ['MUNI_DB'] = environ['MUNI_DB']
#   os.environ['MUNI_DIR'] = environ['MUNI_DIR']
#   return _application(environ, start_response)