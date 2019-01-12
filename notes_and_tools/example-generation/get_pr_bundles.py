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

out_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples'
server_path = 'http://vhdir-demo.fhir.org/fhir'

headers = {
'Accept':'application/fhir+json',
'Content-Type':'application/fhir+json'
}

params = {
'_count':500,
}

# out_folders = ['','20181206-small/','20181206-large/']
out_folders = ['20181206-large/']


# get bundle of VRs 1st one
def get_bundle(snapshot=None, page_num=None):

    params = {
    '_count':500,
    '_snapshot': snapshot,
    '_page':page_num
    }

    #r = get(f'{server_path}/Practitioner', headers=headers, params=params)
    r = get(f'{server_path}/PractitionerRole', headers=headers, params=params)
    return B.Bundle(loads(r.text))


def save_bundle(res,suffix=None):  # res as fhirclient model

    for out_folder in out_folders:

        with open(f'{out_path}/{out_folder}{res.entry[0].resource.resource_type.lower()}/Bundle{suffix}.json', 'w') as f:
            logging.info(f'writing to file = {out_path}/{out_folder}{res.entry[0].resource.resource_type.lower()}/{res.id}.json')
            f.write(dumps(res.as_json(),indent =3))


current_b = get_bundle()
save_bundle(current_b, suffix=str(0))
# save and fetch the next one...
for i in current_b.link:
    print(i.relation, i.url)
    if i.relation == 'last':
        snapshot = (i.url.split('snapshot=')[1]).split('&')[0]
        num_pages = int(i.url.split('&_page=')[1])
        print(snapshot, num_pages)

for i in range(1,num_pages+1):
    print(i)
    current_b = get_bundle(snapshot=snapshot, page_num=i)
    save_bundle(current_b, suffix=str(i))
