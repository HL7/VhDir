# ===================================
# create VHDIR FHIR resources instances from the subset of the nppes data files:
# run in python 3.5 or above
# ====================================

import fhir_example_templates as f_templ
import lat_long_byzip as ll
import rR_dict as rr
import name_generator as names
import taxonomy_codes as t
import csv
import lxml.etree as etree
from random import choice, choices
from pprint import pprint, pformat
from datetime import datetime
import os, sys, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

in_path ='/Users/ehaas/Documents/FHIR/VhDir/notes and tools/example-generation/examples'
out_path = '/Users/ehaas/Documents/FHIR/VhDir/notes and tools/example-generation/examples'
server_path = 'http://test.fhir.org/r4'
in_file = 'sample-nppes-practitioner-data'

type='practitioner'
Type=rr.r_map[type]

usps_map = dict(MA='Massachusetts',CT='Connecticut',RI='Rhode Island')
gender = dict(M='male',F='female')

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

def get_phone1():
    phone0 = item['Provider Business Practice Location Address Telephone Number']
    phone1 = item['Provider Business Mailing Address Telephone Number']
    phone2 = item['Provider Business Practice Location Address Fax Number']
    phone3 = item['Provider Business Mailing Address Fax Number']
    if phone1 and phone1 != phone0:
        return(phone1)
    elif phone2 and phone2 != phone0:
        return(phone2)
    elif phone3 and phone3 != phone0:
        return(phone)
    else:
        return('5555555555')


def get_qual_code_display(code):
    try:
        return(t.taxonomy_codes[code])
    except KeyError:
        return('Taxonomy code display')


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
    random_name = names.get_random_name(item['Provider Gender Code'])[0] #fn returns a list
    logging.debug('random_name ={} and type= {}'.format(random_name,'foo'))
    # create id for file name
    f_id = 'vhdir-{type}-{npi}'.format(
    type=type,
    npi=npi
    )
    logging.info('create resource id = {f_id}'.format(f_id=f_id))
    
    # use fhir xml template to create practitioner qualification instance  TODO create a second instance
    qualification = f_templ.practitioner_qual_template.format(
            license_state=item['Provider License Number State Code_1'],
            license_state_display=usps_map[item['Provider License Number State Code_1']],
            small_state=item['Provider License Number State Code_1'].lower(),
            med_license=item['Provider License Number_1'],
            qual_code=item['Healthcare Provider Taxonomy Code_1'],
            qual_code_system='http://www.wpc.edi.com/taxonomy',
            qual_code_display=get_qual_code_display(item['Healthcare Provider Taxonomy Code_1'])
            )
            
    
    #  create a second  qualification instance if data is present
    if item['Provider License Number_2']:
        qualification1 = f_templ.practitioner_qual_template.format(
                license_state=item['Provider License Number State Code_2'],
                license_state_display=usps_map[item['Provider License Number State Code_2']],
                small_state=item['Provider License Number State Code_1'].lower(),
                med_license=item['Provider License Number_2'],
                qual_code=item['Healthcare Provider Taxonomy Code_2'],
                qual_code_system='http://www.wpc.edi.com/taxonomy',
                qual_code_display=get_qual_code_display(item['Healthcare Provider Taxonomy Code_1'])
                )
        qualification = qualification + qualification1

    
    # use fhir xml template to create practitioner instance
    example = f_templ.practitioner_template.format(
        type=type,
        Type = type.capitalize(),
        f_id=f_id,
        npi=npi,
        active='active', # randomize ?
        fname=random_name[0], # based on Gender
        lname=random_name[1], # based on Gender
        sname=item['Provider Credential Text'],
        phone0=item['Provider Business Practice Location Address Telephone Number'],
        phone1=get_phone1(),
        LAT=ll.lat_long[get_zip(item)][0], # remove the  + 4 for looking up lat and long
        LON=ll.lat_long[get_zip(item)][1],
        address=item['Provider First Line Business Practice Location Address'], #todo add second line
        city=item['Provider Business Practice Location Address City Name'],
        state=item['Provider Business Practice Location Address State Name'],
        zip=item['Provider Business Practice Location Address Postal Code'],
        gender= gender[item['Provider Gender Code']],
        qualification=qualification,  # subtemplate
        communication=choices(f_templ.practitioner_comm_template,weights=[80,20])[0] # skewed random choice of en or en+es
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
logging.debug('batch_bundle ={}'.format(batch_bundle))

write_xml(out_path,type,batch_bundle)  #save to file
    

#This only happens when this module is called directly:
if __name__ == "__main__":

    logging.debug('end of program')

   
# create VHDIR FHIR resources instances using this data