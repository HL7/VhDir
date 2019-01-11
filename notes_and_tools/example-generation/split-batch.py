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

# in_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples/20181206-large/practitioner'
# in_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples/20181206-large/practitionerrole'
in_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples/20181206-large/endpoint'

server_path = 'http://vhdir-demo.fhir.org/fhir'

headers = {
'Accept':'application/fhir+json',
'Content-Type':'application/fhir+json'
}


# *************** Functions *****************

def get_bundle(in_file):  # as py fhir bundle class
    with open(f'{in_path}/{in_file}') as f:
        logging.info(f'reading file = {in_file}')
        return B.Bundle(load(f))

def post_bundle(data):
    r = post(f'{server_path}', headers = headers, data = dumps(data.as_json()))
    logging.info(f'posting {data.id} to {server_path}')
    logging.info(f'server response =  {r.status_code}')
    logging.info(f'server response =  {dumps(r.json(),indent=3)}')

    if r.status_code > 200:
        logging.info(f'server response =  {dumps(r.json(),indent=3)}')


def write_bundle(res):  # res as fhirclient model
    with open(f'{in_path}/{res.id}.json', 'w') as f:
        logging.info(f'writing to file = {in_path}/{res.id}.json')
        f.write(dumps(res.as_json(),indent =3))


prb = get_bundle('vhdr-endpoint-example-bundle.json')


#split into smaller 500 entry bundles and write and post


for k in range(int(len(prb.entry)/500) + 1):
    nb = B.Bundle()
    nb.id = f"{prb.id}-{k}"
    nb.type = "batch"
    nb.entry = []

    for i in range(500):
        try:
            entry = B.BundleEntry(prb.entry[k*500+i].as_json())
            nb.entry.append(entry)
        except IndexError:
            break
    print(k*500+i)
    post_bundle(nb)
    write_bundle(nb)

logging.debug('end of program')
