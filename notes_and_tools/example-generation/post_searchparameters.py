import fhir_example_templates2 as f_templ
import base64_geosjon as b64
import rR_dict as rr
import name_generator as names
import taxonomy_codes as t
import csv
from json import dumps, loads, load, dump
from datetime import datetime, date
from itertools import cycle
from random import choices
from dateutil.relativedelta import *
from stringcase import spinalcase, titlecase, snakecase
from fhirr4models import bundle as B
from fhirr4models import practitioner as P
from fhirr4models import organization as O
from fhirr4models import organizationaffiliation as OA
from fhirr4models import practitionerrole as PR
from fhirr4models import endpoint as EP
from fhirr4models import location as L
from fhirr4models import fhirdate as FD
from fhirr4models import period as PD
from pprint import pformat, pprint
from requests import get, post, put

import os, sys, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

# *************** Globals *******************

#in_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples/20181206-large/endpoint'
#in_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples/20181206-large/verificationresult'
# in_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples/practitioner'
in_path = '/Users/ehaas/Documents/FHIR/VhDir/source/resources'
# server_path = 'http://vhdir-demo.fhir.org/fhir'
# server_path = 'http://vhdir-demo.fhir.org/fhir'
server_path = 'http://sqlonfhir-r4.azurewebsites.net/fhir'


headers = {
'Accept':'application/fhir+json',
'Content-Type':'application/fhir+json'
}

def get_file(in_file):
    with open(f'{in_path}/{in_file}') as f:
        logging.info(f'reading file = {in_file}')
        return f.read()

def post_file(data):
    d_data = loads(data)
    r = put(f'{server_path}/{d_data["resourceType"]}/{d_data["id"]}', headers = headers, data = data)
    logging.info(f'posting {filename} to {server_path}')
    logging.info(f'server response =  {r.status_code}')
    logging.info(f'server response =  {dumps(r.json(),indent=3)}')

# prefix = 'vhdr-endpoint-example-bundle'
# prefix = 'vhdir-vr-examples-bundle'
prefix = 'vhdir-p-examples-bundle'
prefix = 'searchparameter-'
for filename in os.listdir(in_path):
    if filename.startswith(prefix) and filename.endswith('json'):
        file = get_file(filename)
        print(loads(file)['resourceType'])
        post_file(file)



logging.debug('end of program')
