# ===================================
# create VHDIR FHIR resources instances from the subset of the nppes data files:
# run in python 3.5 or above
# ====================================

import fhir_example_templates as f_templ
import lat_long_byzip as ll
import rR_dict as rr
import name_generator as names
import csv
import lxml.etree as etree
from pprint import pprint, pformat
from datetime import datetime
import os, sys, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

in_path ='/Users/ehaas/Documents/FHIR/VhDir/notes and tools/example-generation/examples'
out_path = '/Users/ehaas/Documents/FHIR/VhDir/notes and tools/example-generation/examples'
server_path = 'http://test.fhir.org/r4'
in_file = 'sample-nppes-organization-data'

type='organization'
Type=rr.r_map[type]

try:
    os.mkdir('{out_path}/{type}'.format(out_path=out_path,type=type))
except FileExistsError:
    pass

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


def get_zip(item):
  zip = item['Provider Business Practice Location Address Postal Code']
  if len(zip) <= 5:
    return(zip.lstrip('0'))
  else:
    return(zip[:-4].lstrip('0'))

def get_csv(in_path,in_file):
    with open('{in_path}/{in_file}.csv'.format(in_path=in_path,in_file=in_file)) as f:
       logging.info('reading file = {in_file}'.format(in_file=in_file))
       my_list = [i for i in csv.DictReader(f,fieldnames=None, restkey='id', restval=None, dialect='excel')]
       logging.info('content = {line}'.format(line= pformat(my_list)))
    return(my_list)


def write_xml(out_path,type,file):
    with open('{out_path}/{type}/vhdr-{type}-example-bundle.xml'.format(out_path=out_path, type=type ), 'w') as fxml:
        logging.info('writing to file = {out_path}/{type}/vhdr-{type}-example-bundle.xml'.format(out_path=out_path, type=type ))
        # prettify before saving
        root = etree.fromstring(file)
        fxml.write(etree.tostring(root, pretty_print=True).decode())


#create bundle using xml templates and csv data
entries = ''
# get_csv(in_path,in_file)
for item in get_csv(in_path,in_file):
    
    npi='999{}'.format(item['NPI'][3:])  ##rep;ace first 3 digits of npi with 999 TODO validate to validate with Luhn algorithm ... todo check for dupes
    logging.info('changing npi={old_npi} to npi={new_npi}'.format(old_npi=item['NPI'],new_npi=npi))
    excape_xml(item)# check if need to escape xml character like '&'
    #todo scramble names using names lists
    random_name = names.get_random_name()[0] # fn returns a list of weighted choices
    # create id for file name
    f_id = 'vhdir-{type}-{npi}'.format(
    type=type,
    npi=npi
    )
    logging.info('create resource id = {f_id}'.format(f_id=f_id))
    
    # use fhir xml template to create organization instance
    example = f_templ.organization_template.format(
    type=type,
    f_id=f_id,
    npi=npi,
    name=item['Provider Organization Name (Legal Business Name)'],
    phone=item['Provider Business Practice Location Address Telephone Number'],
    address=item['Provider First Line Business Practice Location Address'], #todo add second line
    city=item['Provider Business Practice Location Address City Name'],
    state=item['Provider Business Practice Location Address State Name'],
    zip=item['Provider Business Practice Location Address Postal Code'],
    LAT=ll.lat_long[get_zip(item)][0], # remove the  + 4 for looking up lat and long
    LON=ll.lat_long[get_zip(item)][1],
    prov_type_code='prov',
    prov_type_display='Healthcare Provider',
    prov_type_text='Healthcare Provider',
    contact_fname=random_name[0],
    contact_lname=random_name[1],
    contactpoint_location_reference='todo',
    contactpoint_location_reference_display='todo'
    )
    
    entry = f_templ.entries_templ.format(server_path=server_path, f_id=f_id, example=example, Type=Type)
    entries = '{entries}\n{entry}'.format(entries=entries, entry=entry)
    
    logging.info('create {type} example: \n{example}'.format(type=type,example=example))
    '''
    # save as examples
    with open('{out_path}/{type}/{type}-{f_id}.xml'.format(type=type,out_path=out_path,f_id=f_id), 'w') as fxml:
        fxml.write(example)
    #logging.info('example = {}'.format(example))
    '''
    
# create batch bundle
timestamp = '{}Z'.format(datetime.utcnow().isoformat())
batch_bundle = f_templ.batch_bundle_template.format(
timestamp=timestamp,
entries=entries, type=type
)
write_xml(out_path,type,batch_bundle)  #save to file
    

#This only happens when this module is called directly:
if __name__ == "__main__":

    logging.debug('end of program')

   
# create VHDIR FHIR resources instances using this data