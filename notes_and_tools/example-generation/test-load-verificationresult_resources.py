# ===================================
# create VHDIR FHIR resources instances using the the subset of the nppes data files:
# run in python 3.6 or above
# see requirements.txt for modules
# this set of examples is produced using fstrings in json and validated using the python-client models
# ====================================

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

in_path ='/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/sample-nppes-data'
out_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples'
server_path = 'http://vhdir-demo.fhir.org/fhir'
convert_server = 'http://wildfhir.aegis.net/fhir3-5-0'
fhir_test_server = 'http://wildfhir.aegis.net/fhir3-5-0'

headers = {
'Accept':'application/fhir+json',
'Content-Type':'application/fhir+json'
}

# out_folders = ['','20181206-small/','20181206-large/']
out_folders = ['20181206-large/']

'''
example_files = dict(
orgs = '20181206-small/organization/vhdr-organization-example-bundle',
practs = '20181206-small/practitioner/vhdr-practitioner-example-bundle',
managing_orgs = '20181206-small/managing-org/vhdr-organization-managing-org-example-bundle',
pract_roles = '20181206-small/practitionerrole/vhdr-practitionerrole-example-bundle',
hie_org_roles = '20181206-small/hie-orgaffiliation/vhdr-organizationaffiliation-hie-orgaffiliation-example-bundle',
hc_services = '20181206-small/healthcareservice/vhdr-organization-healthcareservice-example-bundle',
networks ='20181206-small/network/vhdr-network-example-bundle',
org_roles = '20181206-small/organizationrole/vhdr-organizationrole-example-bundle',
locations = '20181206-small/location/vhdr-organization-location-example-bundle',
endpoints = '20181206-small/endpoint/vhdr-endpoint-example-bundle',
insuranceplans = '20181206-small/insuranceplan/vhdr-insuranceplan-example-bundle',
)
'''
example_files = dict(
verresults = '20181206-large/verificationresult/Bundle1'
)


q_status_codes= [
    ('active', 'active'),
    ('inactive', 'inactive'),
    ('issued-in-error', 'issued in error'),
    ('revoked', 'revoked'),
    ('pending', 'pending'),
    ('unknown', 'unknown')
     ]

date = date.today()


def get_bundle(in_path, in_file):  # as python model
    with open(f'{in_path}/{in_file}.json') as f:
        logging.info(f'reading file = {in_file}')
        return B.Bundle(load(f))

#orgs = get_bundle(out_path, org_file)
#parent_orgs = get_bundle(out_path, managing_org_file)
#pract_roles = get_bundle(out_path, pract_org_file)
#{x: x**2 for x in (2, 4, 6)}
#bundles = {k:get_bundle(out_path,v) for k,v in example_files.items()}


def get_csv(in_path,in_file):
    with open(f'{in_path}/{in_file}.csv') as f:
        logging.info(f'reading file = {in_file}')
        my_list = [j for j in csv.DictReader(f, restkey='foo_id', restval=None, dialect='excel')]
    return my_list


def get_bundle(in_path, in_file):  # as py fhir bundle class
    with open(f'{in_path}/{in_file}.json') as f:
        logging.info(f'reading file = {in_file}')
        return B.Bundle(load(f))

def scrub_dict(d):
    unwanted = ['', u'', None, [], {}, 'None', -1]
    if type(d) is dict:
        return dict((k, scrub_dict(v)) for k, v in d.items() if v not in unwanted and scrub_dict(v))
    elif type(d) is list:
        return [scrub_dict(v) for v in d if v not in unwanted and scrub_dict(v)]
    else:
        return d


def get_xml(server, body, type):
    from requests import put,get
    from xml.etree import ElementTree

    x_headers ={
    'Content-Type':'application/fhir+xml',
    'Accept':'application/fhir+xml'
    }
    j_headers ={
    'Content-Type':'application/fhir+json',
    'Accept':'application/fhir+json'
    }
    x_params ={
        '_count':500
        }

    r = put(url=f'{server}/Bundle/vhdir-{type}-examples-bundle', data=body.encode('utf-8'), headers=j_headers)
    logging.info(f'put json status_code = {r.status_code}')
    logging.info(f'body as json = \n{dumps(r.json(), indent =3)}')

    r = get(url=f'{server}/Bundle/vhdir-{type}-examples-bundle', headers=x_headers, params=x_params)
    logging.info(f'get xml status_code = {r.status_code}')
    return r.content  # may not work if large


def write_bundle(res):  # res as fhirclient model

    for out_folder in out_folders:
        try:
            os.mkdir(f'{out_path}/{out_folder}{res.entry[0].resource.resource_type.lower()}')
        except FileExistsError:
            pass

        with open(f'{out_path}/{out_folder}{res.entry[0].resource.resource_type.lower()}/{res.id}.json', 'w') as f:
            logging.info(f'writing to file = {out_path}/{out_folder}{res.entry[0].resource.resource_type.lower()}/{res.id}.json')
            f.write(dumps(res.as_json(),indent =3))


def write_resource_csv(f_type,data):
    for out_folder in out_folders:
        with open(f'{out_path}/{out_folder}{f_type}/sample-nppes-{f_type}-data.csv', mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, dialect='excel', quoting=csv.QUOTE_ALL)
            writer.writerow(['NPI','Resource ID','Name','References List'])
            for line in data:
                writer.writerow(line)

# *********************** validate Resource ********************************
def validate_res(res,profile):
        params = {
        'profile': profile
        }
        #   r = requests.post('https://httpbin.org/post', data = {'key':'value'})
        r = post(f'{fhir_test_server}/{res.resource_type}/$validate', params = params, headers = headers, data = dumps(res.as_json()))
        # print(r.status_code)
        # view  output
        logging.info(f'Validation output = {dumps(r.json(),indent =3)}')

#****************  Main  *************************

def update_vr(f_type,suffix,id_list):
    Type=rr.r_map[f_type]
    mo = cycle([i for i in range(1,5)])

    profile = 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-validation'

    vr_status_codes = [
    'attested', # next scheduled in 6 months
    'validated', # next scheduled in 6 months
    'in-process', # date recent within last 2 weeks
    'req-revalid', # next scheduled in 1 month
    'val-fail', # next scheduled in 10 days
    'reval-fail' # next scheduled in 10 days
    ]
    # get bundle of VR files
    #bundles = {k:get_bundle(out_path,v) for k,v in example_files.items()}
    #logging.info(f'bundle = {bundles}')

    vr_bundle = get_bundle(out_path,f'20181206-large/{f_type}/Bundle{suffix}')
    #change to batch bundle
    vr_bundle.id = f'vhdir-vr-examples-bundle-{vr_bundle.id.split("urn:uuid:")[1]}'
    vr_bundle.meta = None
    vr_bundle.type = 'batch'
    vr_bundle.link = None
    vr_bundle.count = None

    # update all the statuses
    for entry in vr_bundle.entry:
        id_list.append((entry.resource.id,f'VerificationResult/{entry.resource.id}',entry.resource.primarySource[0].who.reference))
        #randomize the statuses
        vr_status = choices(vr_status_codes,weights = [15,60,5,5,10,5])[0]

        logging.info(f'status = {entry.resource.status}')
        entry.resource.status = vr_status
        logging.info(f'status = {entry.resource.status}')

        #update these statusDate == lastPerformed to be in range of last six months.  and
        # these are independent from qual dates.  .. for now
        if vr_status in ['attested','validated']:
            status_date = date + relativedelta(months=-next(mo))
            next_date = status_date + relativedelta(months=+6)
        elif vr_status == 'in-process':
            status_date = date + relativedelta(days=-next(mo))
            next_date = status_date + relativedelta(months=+6)
        elif vr_status == 'req-revalid':
            status_date = date + relativedelta(months=-6)
            next_date = date + relativedelta(months=+1)
        elif vr_status in ['val-fail','reval-fail']:
            status_date = date + relativedelta(months=-next(mo))
            next_date = date + relativedelta(days=+10)

        logging.info(f'status date = {entry.resource.statusDate.as_json()}')
        entry.resource.statusDate = FD.FHIRDate(str(status_date))
        logging.info(f'status date = {entry.resource.statusDate.as_json()}')

        logging.info(f'last performed date = {entry.resource.lastPerformed.as_json()}')
        entry.resource.lastPerformed = FD.FHIRDate(str(status_date))
        logging.info(f'last performed date = {entry.resource.lastPerformed.as_json()}')

        logging.info(f'next scheduled date = {entry.resource.nextScheduled.as_json()}')
        entry.resource.nextScheduled = FD.FHIRDate(str(next_date))
        logging.info(f'next scheduled date = {entry.resource.nextScheduled.as_json()}')

        #update bundle to batch bundle:

        entry.request = B.BundleEntryRequest()
        entry.request.method = 'PUT'
        entry.request.url = f'VerificationResult/{entry.resource.id}'




    write_bundle(vr_bundle)

    # validate_res(vr_bundle, profile)  # no validation for

    write_resource_csv(f_type,id_list)


#********************* __name__ == "__main__" ********************

#This only happens when this module is called directly:
if __name__ == "__main__":
    id_list=[]
    for i in range(0,8):
        update_vr('verificationresult',str(i),id_list)
# main('practitioner')

    logging.debug('end of program')
