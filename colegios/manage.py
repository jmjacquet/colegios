#!/usr/bin/env python
import os
import sys
from django.utils.log import getLogger
from django.core.management import execute_from_command_line

logger = getLogger('management_commands')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "colegios.settings")
    os.environ['MUNI_ID'] = '150'
    os.environ['MUNI_DB'] = 'grupogua_colegioto'
    os.environ['MUNI_DIR'] = 'santafe'
    # os.environ['MUNI_ID'] = '151'
    # os.environ['MUNI_DB'] = 'grupogua_colegioto_ros'
    # os.environ['MUNI_DIR'] = 'rosario'
    
    execute_from_command_line(sys.argv)
    # try:
    # 	from django.core.management import execute_from_command_line
    # 	execute_from_command_line(sys.argv)
    # except Exception as e:
    #     logger.error('Admin Command Error: %s', ' '.join(sys.argv), exc_info=sys.exc_info())
    #     raise e

    