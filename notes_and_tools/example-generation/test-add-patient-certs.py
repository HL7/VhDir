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
from fhirr4models import extension as X

from pprint import pformat, pprint
from requests import get, post, put

import os, sys, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')



# *************** Globals *******************

in_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples/20181206-large/practitioner'
out_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples/practitioner'
# in_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples/20181206-large/practitionerrole'
date = date.today()
mo = cycle(range(1,12))
# *************Templates ********************

def get_epx(id,name):

    return {
          'url' : 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/endpoint-reference',
          'valueReference' : {
            'reference' : f'Endpoint/{id}',
            'display' : f'{name} Direct address'
          }
        }

def get_certx():

    exp_date = date + relativedelta(months=-6) + relativedelta(months=next(mo)) # cycle through 12 months


    return  {
          'url' : 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/digitalcertificate',
          'extension' : [
            {
              'url' : 'type',
              'valueCoding' : {
                'system' : 'http://hl7.org/fhir/uv/vhdir/CodeSystem/digitalcertificate',
                'code' : 'ind',
                'display' : 'Individual'
              }
            },
            {
              'url' : 'use',
              'valueCoding' : {
                'system' : 'http://hl7.org/fhir/uv/vhdir/CodeSystem/digitalcertificate',
                'code' : 'signing',
                'display' : 'Signing'
              }
            },
            {
              'url' : 'certificateStandard',
              'valueCoding' : {
                'system' : 'http://hl7.org/fhir/uv/vhdir/CodeSystem/digitalcertificate',
                'code' : 'x.509v3',
                'display' : 'x.509v3'
              }
            },
            {
              'url' : 'certificate',
              'valueString' : 'TXkgbmFtZSBpcyBHZW9yZ2UgV2FzaGluZ3Rvbi4gVGhpcyBpcyBteSBjZXJ0aWZpY2F0ZS4gDQoNCi0tLS0tQkVHSU4gUFVCTElDIEtFWS0tLS0tDQpNSUdlTUEwR0NTcUdTSWIzRFFFQkFRVUFBNEdNQURDQmlBS0JnRkZLcjVGazJla2dYSjdwUXpKVzBWdm9NZzQ4DQpldk1DTUFTbk95M09rS1VyZlIwSGZHTmRUS216L3VpcWVjOGR3U1E5NFpKR3Njd3FzczVScmtYNkEzUHZsZmM3DQpkdlJNQlBxYzdsKzRrOHN5b2t4bzh4SW8vN0hLOE1kWW45dlhId1k5VWxGZDduRjZsbWN0Nzd3THMxNWdrZjN1DQpHVXErZ1RDV3hnZlYzbm05QWdNQkFBRT0NCi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQ=='
            },
            {
              'url' : 'expirationDate',
              'valueDate' :  str(exp_date)
            },
            {
              'url' : 'trustFramework',
              'valueCodeableConcept' : {
                'coding' : [
                  {
                    'system' : 'http://hl7.org/fhir/uv/vhdir/CodeSystem/digitalcertificate',
                    'code' : 'direct',
                    'display' : 'DirectTrust',
                    'userSelected' : True
                  }
                ]
              }
            }
          ]
        }

# *************** Functions *****************

def get_bundle(in_file):  # as py fhir bundle class
    with open(f'{in_path}/{in_file}') as f:
        logging.info(f'reading file = {in_file}')
        return B.Bundle(load(f))

def write_bundle(res):  # res as fhirclient model
    with open(f'{out_path}/{res.id}.json', 'w') as f:
        logging.info(f'writing to file = {out_path}/{res.id}.json')
        f.write(dumps(res.as_json(),indent =3))

# prefix = 'vhdr-endpoint-example-bundle'
# prefix = 'vhdir-vr-examples-bundle'
prefix = 'vhdir-p-examples-bundle'
for filename in os.listdir(in_path):
    if filename.startswith(prefix) and filename.endswith('json'):
        bundle = get_bundle(filename)
        #print(file)

        # fix code system error
        'http://hl7.org/fhir/uv/vhdir/CodeSystem/credentialstatus'

        # add cert extension with varying expirations

        for entry in bundle.entry:


            patient = entry.resource

            # fix code system error
            for qual in patient.qualification:
                qual.extension[0].extension[0].valueCoding.system = 'http://hl7.org/fhir/uv/vhdir/CodeSystem/credentialstatus'

            # add cert extension with varying expirations
            patient.extension = []
            certificate = X.Extension(get_certx())
            patient.extension.append(certificate)


        #write_bundle(bundle)

logging.debug('end of program')
