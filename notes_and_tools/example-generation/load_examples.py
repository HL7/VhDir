
from json import dumps, loads, load, dump
from fhirr4models import bundle as B
from pprint import pformat, pprint
from requests import get, post, put

import os, sys, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')



# *************** Globals *******************

# in_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples/20181206-large/practitioner'
# in_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples/20181206-large/practitionerrole'
in_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples/20181206-large'

#server_path = 'http://vhdir-demo.fhir.org/fhir'
server_path = 'http://wildfhir.aegis.net/fhir3-5-0'

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


def write_bundle(res):  # res as fhirclient model
    with open(f'{in_path}/{res.id}.json', 'w') as f:
        logging.info(f'writing to file = {in_path}/{res.id}.json')
        f.write(dumps(res.as_json(),indent =3))

def split_bundle(file):#split into smaller 500 entry bundles and write and post
    for k in range(int(len(file.entry)/500) + 1):
        nb = B.Bundle()
        nb.id = f"{file.id}-{k}"
        nb.type = "batch"
        nb.entry = []
        for i in range(500):
            try:
                entry = B.BundleEntry(file.entry[k*500+i].as_json())
                nb.entry.append(entry)
            except IndexError:
                break
        print(k*500+i)
        logging.info(f'posting bundle {file.id}...entries {k*500}-{k*500+i}')
        post_bundle(nb)


for folder in os.listdir(in_path):
    if os.path.isdir :
        for filename in os.listdir(f'{in_path}/{folder}'):
            if filename.endswith('json'):
                file = get_bundle(f'{folder}/{filename}')
                if len(file.entry) > 500:
                    logging.info('splitting bundle...')
                    split_bundle(file)
                else:
                    logging.info(f'posting bundle...{filename}')
                    post_bundle(file)

logging.debug('end of program')
