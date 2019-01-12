from json import load, loads, dumps
import requests

from fhirr4models import bundle as B
from fhirr4models import endpoint as EP

import os, sys, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

#***********Globals******************

#test_type = 'endpoints'
#Type = 'Endpoint'
#test_type = 'managing_orgs'
#Type = 'Organization'
test_type = 'insuranceplans'
Type = 'InsurancePlan'
#test_type = 'networks'
#Type = 'Organization'
#test_type = 'org_roles'
#Type = 'OrganizationAffiliation'
#test_type = 'pract_roles'
#Type = 'PractitionerRole'

headers ={
'Content-Type':'application/fhir+json',
'Accept':'application/fhir+json'
}

in_path ='/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/sample-nppes-data'
out_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples'
#server_path = 'http://vhdir-demo.fhir.org/fhir'
server_path = 'http://wildfhir.aegis.net/fhir3-5-0'

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




#***************  referenced Org bundles ******

def get_bundle(in_path, in_file):  # as python model
    with open(f'{in_path}/{in_file}.json') as f:
        logging.info(f'reading file = {in_file}')
        return B.Bundle(load(f))

#orgs = get_bundle(out_path, org_file)
#parent_orgs = get_bundle(out_path, managing_org_file)
#pract_roles = get_bundle(out_path, pract_org_file)
#{x: x**2 for x in (2, 4, 6)}
bundles = {k:get_bundle(out_path,v) for k,v in example_files.items() if k == test_type}

pyfhir_data = bundles[test_type].entry[0].resource

logging.info(f'pyfhir_data = \n {dumps(pyfhir_data.as_json(),indent = 3)}')

fhir_data=dumps(pyfhir_data.as_json())

#request to server_path to validate
r = requests.post(url=f'{server_path}/{Type}/$validate', data=fhir_data, headers=headers)

logging.info(f'status_code = {r.status_code}')
logging.info(f'headers = {r.headers}')
# logging.info(f'body as raw = {r.raw}')
logging.info(f'body as json = \n{dumps(r.json(), indent =3)}')
logging.info(f'body as html text = \n{r.json()["text"]["div"]}')

# view text in browser
with open(f'{out_path}/validate_text.html','w') as f:
    logging.info('writing validation text to file to display')
    f.write(f'<!DOCTYPE html><html><head><title>Page Title</title></head><body><h1>Validation output</h1>{r.json()["text"]["div"]}</body></html>')
os.system("open "+"/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples/validate_text.html")
