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
from fhirclient.models import bundle as B
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

# in_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples/20181206-large/practitioner'
# in_path = '/Users/ehaas/Documents/FHIR/FHIR Experience/'
in_path = '/Users/ehaas/Documents/Python/MyNotebooks/Q-maker/'
#in_file = 'proles.json'
in_file = 'qr_search_batch.json'

# *************** Functions *****************

def get_bundle():  # as py fhir bundle class
    with open(f'{in_path}{in_file}') as f:
        logging.info(f'reading file = {in_file}')
        return B.Bundle(load(f))

def write_bundle(res):  # res as fhirclient model
    with open(f'{in_path}/{res.id}.json', 'w') as f:
        logging.info(f'writing to file = {in_path}/{res.id}.json')
        f.write(dumps(res.as_json(),indent =3))


p_bundle = get_bundle()

#change to batch bundle
p_bundle.id = 'qr_batch_bundle'
p_bundle.meta = None
p_bundle.type = 'batch'
p_bundle.link = None
p_bundle.count = None
#pd = []
for entry in p_bundle.entry:

    #update bundle to batch bundle:

    entry.request = B.BundleEntryRequest()
    entry.request.method = 'PUT'
    entry.request.url = f'QuestionnaireResponse/{entry.resource.id}'
    '''
    r = entry.resource
    d = dict(
    practitioner = r.practitioner.display,
    practitioner_url = r.practitioner.reference,
    organization = r.organization.display,
    organization_url = r.organization.reference,
    location = r.location[0].display,
    location_url = r.location[0].reference,
    specialty_code = r.specialty[0].coding[0].code,
    specialty = r.specialty[0].coding[0].display,
    endpoint = r.endpoint[0] if r.endpoint else None
    )
    '''
    #pd.append(d)

write_bundle(p_bundle)
'''
keys = pd[0].keys()
with open(f'{in_path}/argo-pd.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(pd)
'''

logging.debug('end of program')
