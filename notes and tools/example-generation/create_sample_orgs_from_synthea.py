# ===================================
# create VHDIR FHIR resources instances using this data
# run in python 3.5 or above
# ====================================
''' sample dict structure  created from the synthea resource files:

 {'': '7',
  'LAT': '33.273307',
  'LON': '-86.806454',
  'address': '1000 FIRST STREET NORTH',                     
  'city': 'ALABASTER',
  'county': 'SHELBY',
  'emergency': 'Yes',
  'id': '010016',
  'name': 'SHELBY BAPTIST MEDICAL CENTER',
  'npi': '9990000007',  # generated see below
  'ownership': 'Voluntary non-profit - Private',
  'org-type': 'hospital'  #  add based on the synthea resource file
  'phone': '2056208100',
  'quality': '3',
  'state': 'AL',
  'zip': '35007'
  }
  
 also need these variables
type_vars = dict( 
org_type_display = 'Healthcare Provider',
org_type_code = 'prov',
org_type_text = 'Hospital',
org-type_id = org_type
)

'''

import fhir_example_templates as f_templ
import lat_long_byzip as ll
import rR_dict as rr
import csv
from pprint import pprint, pformat
from datetime import datetime
import os, sys, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

# in_path ='/Users/ehaas/Downloads/'
in_path ='/Users/ehaas/Documents/FHIR/VhDir/synthea/src/main/resources/providers'
#in_path = '/Users/ehaas/Documents/FHIR/VhDir/source/pre_mustsupport_profiles'
out_path = '/Users/ehaas/Documents/FHIR/VhDir/notes and tools/example-generation/examples'
server_path = 'http://test.fhir.org/r4'
in_file = 'hospitals'

res_type = 'organization'
Type=rr.r_map[res_type]
try:
    os.mkdir('{out_path}/{res_type}'.format(out_path=out_path,res_type=res_type))
except FileExistsError:
    pass
# max number of fhir_example
max_num = 100
prov_type = in_file.split('.')[0].split('/')[-1][:-1]  # make singular
type_vars = dict( 
prov_type = prov_type,
prov_type_display = 'Healthcare Provider',
prov_type_code = 'prov',
prov_type_text = prov_type.capitalize()
)

escape_map = {
'&': '&amp;',
"'": '&apos;',
'>': '&gt;',
'<': '&lt;',
'"': '&quot;'
}


def excape_xml(item):  # check for xml characters and escape
    for key in item:
        for k,v in escape_map.items():
            item[key] = item[key].replace(k,v)
    return(item)

def get_zip(zip):
  zip = item['Provider Business Practice Location Address Postal Code']
  if len(zip) <= 5:
    return(zip)
  else:
    return(zip[:-4])


logging.info('type_vars = {}'.format(type_vars))

with open('{in_path}/{in_file}.csv'.format(in_path=in_path,in_file=in_file)) as f:
   my_list = [i for i in csv.DictReader(f,fieldnames=None, restkey='id', restval=None, dialect='excel')]

logging.info((pformat(my_list[0:max_num])))
#make npi as 999 + id padded with leading zero to make length equal TODO validate to validate with Luhn algorithm

#create bundle using xml templtate and csv data
entries = ''
for item in my_list[0:max_num]:
    excape_xml(item)# check if need to escape xml character like '&'
    item['npi'] = '999{}'.format(item['id'][4:].zfill(7)) 
    f_id = 'vhdir-{prov_type}-{npi}'.format(**item, **type_vars)
    example = f_templ.organization_template.format(**type_vars, **item)
    entry = f_templ.entries_templ.format(server_path=server_path, f_id=f_id, example=example, Type=Type)
    entries = '{entries}\n{entry}'.format(entries=entries, entry=entry)
    
    '''
    # save as examples
    with open('{out_path}/{res_type}/{res_type}-{f_id}.xml'.format(res_type=res_type,out_path=out_path,f_id=f_id), 'w') as fxml:
        fxml.write(example)
    #logging.info('example = {}'.format(example))
    '''
    
# create batch bundle
timestamp = '{}Z'.format(datetime.utcnow().isoformat())
batch_bundle = f_templ.batch_bundle_template.format(timestamp=timestamp,entries=entries, **type_vars)
with open('{out_path}/{res_type}/vhdr-{prov_type}-example-bundle.xml'.format(out_path=out_path, res_type=res_type, **type_vars), 'w') as fxml:
        fxml.write(batch_bundle)

    


# create examples


logging.debug('end of program')

   
# create VHDIR FHIR resources instances using this data