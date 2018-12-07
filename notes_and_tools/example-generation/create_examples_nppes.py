
# ===================================
# create VHDIR FHIR resources instances from the subset of the nppes data files:
# run in python 3.5 or above
# see requirements.txt for modules
# ====================================

import fhir_example_templates as f_templ
import lat_long_byzip as ll
import rR_dict as rr
import name_generator as names
import taxonomy_codes as t
from nucc_dict import nucc_dict
from nucc_maps import nucc_healthcareservice_map, healthcareservice_list, nucc_role_map, nucc_sct_specialty_map, nucc_sct_role_map
import csv
import string
import lxml.etree as etree
from random import choice, choices, randint, sample
from pprint import pprint, pformat
from datetime import datetime
from stringcase import spinalcase, titlecase, snakecase

import os, sys, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

#***********Globals******************

in_path ='/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/sample-nppes-data'
out_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples'
server_path = 'http://test.fhir.org/r4'


#***********Global modified NPPES ORG and PRACT extracts******************

def make_new_npi(old_npi):
        new_npi='999{}'.format(old_npi[3:])  ##rep;ace first 3 digits of npi with 999 TODO validate to validate with Luhn algorithm ... todo check for dupes
        logging.info('changing npi={old_npi} to new npi={new_npi}'.format(old_npi=old_npi,new_npi=new_npi))
        return(new_npi)
        
        
def make_new_name(gender=None):        
        #todo scramble names using names lists
        random_name = names.get_random_name()[0] # fn returns a list of weighted choices
        logging.debug('random_name ={}'.format(random_name))
        try:
            random_name = names.get_random_name(gender)[0] #fn returns a list
            logging.debug('random_gendered_name ={}'.format(random_name))
        except KeyError:
            pass
        return(random_name)
        
def escape_xml(item): # check for xml characters and escape
    escape_map = {
    '&': '&amp;',
    "'": '&apos;',
    '>': '&gt;',
    '<': '&lt;',
    '"': '&quot;'
    }  
    for key in item:
        for k,v in escape_map.items():
            item[key] = item[key].replace(k,v)
    return(item)


def get_csv(in_path,type):
    max = 2000
    in_file = 'sample-nppes-{type}_20181204-data.csv'.format(type=type)
    with open('{in_path}/{in_file}'.format(in_path=in_path,in_file=in_file)) as f:
        logging.info('reading file = {in_file}'.format(in_file=in_file))
        my_list = [j for i,j in enumerate(csv.DictReader(f,fieldnames=None, restkey='id', restval=None, dialect='excel')) if i < max]
        # logging.info('content = {line}'.format(line= pformat(my_list)))
        try:
            for i in my_list:  #update npis
                i['NPI'] = make_new_npi(i['NPI'])
                if type=='organization':  # Randomize names
                    random_name=make_new_name()
                    i['Authorized Official First Name']=random_name[0]
                    i['Authorized Official Last Name']=random_name[1]
                if type=='practitioner':
                    random_name=make_new_name(i['Provider Gender Code'])
                    i['Provider First Name']=random_name[0]
                    i['Provider Last Name (Legal Name)']=random_name[1]
                escape_xml(i)
        except :  # network
            pass



       # logging.info('updated row = {i}'.format(i=pformat(i)))
            
    return(my_list)

#**********************************************

org_list = get_csv(in_path,'organization') # organization data gleaned from NPPES
pract_list = get_csv(in_path,'practitioner') # practitioner data gleaned from NPPES
network_list= get_csv(in_path,'network') # made up network data

#**********************************************

#***********more Globals******************

# state specific data (Name,license system ( i made up),licencing body name)
usps_map = dict(
MA=('Massachusetts','https://www.mass.gov/orgs','Board of Registration in Medicine (BORIM)'),
CT=('Connecticut','https://ct.gov/DPH','Connecticut Medical Examining Board'),
RI=('Rhode Island','http://health.ri.gov','State of Rhode Island Department of Health')
)
gender = dict(M='male',F='female')

# hospital systems randomly assign to organizations
hosp_systems = {
'King Hospital System': '9990010000',
'Acme Healthcare': '9990020000',
'Blue Hope': '9990030000',
'None': ''
}

#***************  Functions *********************

def get_f_id(type,npi,source=None):
    if source:
        type = '{source}-{type}'.format(source=source,type=type)
    return('vhdir-{type}-{npi}'.format(
        type=type,
        npi=npi
        ))


def urlify(s):
    for c in string.punctuation:
        s= s.replace(c,'')
    s = s.lower()
    s = spinalcase(s)
    return('https://{url_name}.com'.format(url_name=s))



def get_phone1(item):
    phone0 = item['Provider Business Mailing Address Telephone Number']
    phone2 = item['Provider Business Practice Location Address Telephone Number']
    phone3 = item['Provider Business Practice Location Address Fax Number']
    phone1 = item['Provider Business Mailing Address Fax Number']
    if phone1 and phone1 != phone0:
        return(phone1)
    elif phone2 and phone2 != phone0:
        return(phone2)
    elif phone3 and phone3 != phone0:
        return(phone3)
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


def get_zip(postal_code):  # get 5 digit code
  if len(postal_code) <= 5:
    return(postal_code.lstrip('0'))
  else:
    return(postal_code[:-4].lstrip('0'))


def write_xml(out_path,type,file,source=None):
    if source:
        r_type = '{source}-{type}'.format(source=source,type=type)
    else:
        r_type = type
        
    with open('{out_path}/{type}/vhdr-{r_type}-example-bundle.xml'.format(out_path=out_path, type=type, r_type=r_type ), 'w') as fxml:
        logging.info('writing to file = {out_path}/{type}/vhdr-{type}-example-bundle.xml'.format(out_path=out_path, type=type ))
        # prettify before saving
        parser = etree.XMLParser(remove_blank_text=True)
        root = etree.fromstring(file, parser=parser)
        fxml.write(etree.tostring(root, pretty_print=True).decode())
        
def write_resource_csv(type,data):
    with open('{out_path}/{type}/sample-nppes-{type}-data.csv'.format(out_path=out_path,type=type), mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, dialect='excel', quoting=csv.QUOTE_ALL)
        writer.writerow(['NPI','Resource ID','Name','References List'])
        for line in data:
            writer.writerow(line)


def get_prov_identifier(pract_id=None):
    n = 7
    if pract_id:
        return(pract_id)
    else:
        s = ''.join([str(randint(0, 9)) for num in range(0, n)])
        return(s)


def get_org(state,postal_code):  # gert o rg based on state and closest zip
    distance_list=[]
    pract_zip = get_zip(postal_code)  # normalize to 5 digit zip
    for item in org_list:
        #create new list (distance, NPI) 
        if state == item['Provider Business Practice Location Address State Name']:
            org_zip = get_zip(item['Provider Business Practice Location Address Postal Code'])
            # logging.info('pract_zips= {pract_zip} org_zip = {org_zip} diff = {diff}'.format(pract_zip=pract_zip,org_zip=org_zip,diff=abs(int(pract_zip) - int(org_zip))))
            distance_list.append((abs(int(pract_zip) - int(org_zip)),item['NPI'],item['Provider Business Practice Location Address State Name'],item))

    distance_list.sort(key=lambda tup: tup[0]) #sort list by first item in tuple
            
    # logging.info('org_choices= {org_choices}'.format(org_choices=[i[0:2] for i in distance_list]))
    # randomly assign to 1-3 orgs
    org_item = [i[3] for i in distance_list[0:choice([1,2,3])]]
    # logging.info('org_item = {org_item}'.format(org_item=org_item))
    return(org_item)  # return list of org items
    
    
def get_network(state,all=False):  # get network based on state
    network_item = [item for item in network_list if item['state'] == state]
    if all:
        return network_item
    else:
        return sample(network_item,k=choice([1,2,3]))  # return list of randomly assign to 1-3 networks network items



def get_practrole_code(nucc):
    try:
        return(nucc_role_map[nucc][0])
    except KeyError:
        return('208000000X')


def get_practrole_display(nucc):
    try:
        return(nucc_role_map[nucc][1])
    except KeyError:
        return('Allopathic and Osteopathic Physicians')


def get_practspecialty_code(nucc):
    try:
        return(nucc_role_map[nucc][1])
    except KeyError:
        return('Allopathic and Osteopathic Physicians')

def get_specialty_display(nucc): 
    d1=nucc_dict[nucc][2]
        
    d2=nucc_dict[nucc][3]
    if d2:
        specialty_display = '{d1}/{d2}'.format(d1=d1,d2=d2)
        #logging.info('Map to NUCC specialty  code = {k} NUCC_specialty = {s}'.format(k=k,s=s2))
    elif d1:
        specialty_display = d1
        #logging.info('Map to NUCC specialty  code = {k} NUCC specialty = {s}'.format(k=k,s=s1))
    else:
        specialty_display = 'general practice'
        #logging.info('Map to NUCC specialty  code = {k} NUCC specialty = {s}'.format(k=k,s='general practice'))
    return(specialty_display)


def get_addl_snomed_code_coding(nucc):
    try:
        return(f_templ.addl_snomed_coding_template.format(
        specialty_code=nucc_sct_role_map[nucc][0],
        specialty_display=nucc_sct_role_map[nucc][1]
        ))
    except KeyError:
        return('')


def get_addl_snomed_specialty_coding(nucc):
    try:
        return(f_templ.addl_snomed_coding_template.format(
        specialty_code=nucc_sct_specialty_map[nucc][0],
        specialty_display=nucc_sct_specialty_map[nucc][1]
        ))
    except KeyError:
        return('')


def get_addl_specialty(nucc):
    if nucc:
        return(f_templ.addl_specialty_template.format(
        specialty_code=nucc,
        specialty_display=get_specialty_display(nucc),
        addl_snomed_specialty_coding=get_addl_snomed_specialty_coding(nucc),
        ))
    else:
        return('')

def get_hcs_code(nucc):
    try:
        return(spinalcase(nucc_healthcareservice_map[nucc]))
    except KeyError:
        return('miscellaneous')


def get_hcs_display(nucc):
    try:
        return(titlecase(nucc_healthcareservice_map[nucc]))
    except KeyError:
        return('Miscellaneous')


def orgrole_example(item,f_id,type,network_npi,network_name,managing_org_id,managing_org_name):
        return(f_templ.organizationrole_template.format(
        type=type,
        f_id=f_id,
        identifier_system=urlify(managing_org_id),
        identifier_value=get_prov_identifier(),
        identifier_assigner='identifier_assigner', #todo
        identifier_assigner_display=managing_org_name,
        network_npi=network_npi ,
        network_name=network_name,
        org_npi=item['NPI'],
        org_name=item['Provider Organization Name (Legal Business Name)'],
        ))


def practrole_example(pract_item,f_id,type,pract_npi,org_npi,org_name): # need to assign org before creating
    return(f_templ.practitionerrole_template.format(
    type=type,
    f_id=f_id,
    pract_npi=pract_npi,
    identifier_system=urlify(org_name),
    identifier_value=get_prov_identifier(pract_item['Other Provider Identifier_1']),
    identifier_assigner='identifier_assigner', #todo
    identifier_assigner_display='identifier_assigner_display',  #todo
    fname=pract_item['Provider First Name'], # based on Gender
    lname=pract_item['Provider Last Name (Legal Name)'], # based on Gender
    sname=pract_item['Provider Credential Text'],
    org_npi=org_npi,
    org_name=org_name,
    type_code=get_practrole_code(pract_item['Healthcare Provider Taxonomy Code_1']),
    type_code_display=get_practrole_display(pract_item['Healthcare Provider Taxonomy Code_1']),
    specialty_code=pract_item['Healthcare Provider Taxonomy Code_1'],
    specialty_display=get_specialty_display(pract_item['Healthcare Provider Taxonomy Code_1']),
    addl_snomed_code_coding=get_addl_snomed_code_coding(pract_item['Healthcare Provider Taxonomy Code_1']),
    addl_snomed_specialty_coding=get_addl_snomed_specialty_coding(pract_item['Healthcare Provider Taxonomy Code_1']),
    addl_specialty=get_addl_specialty(pract_item['Healthcare Provider Taxonomy Code_2']),
    hcs_code=get_hcs_code(pract_item['Healthcare Provider Taxonomy Code_1']),
    HCS_Name=get_hcs_display(pract_item['Healthcare Provider Taxonomy Code_1']),
    location_phone=pract_item['Provider Business Practice Location Address Telephone Number']
    ))


def practrole_network_example(pract_item,f_id,type,pract_npi,org_npi,org_name,managing_org_id,managing_org_name): # need to assign org before creating
    return(f_templ.practitionerrole_network_template.format(
    type=type,
    f_id=f_id,
    pract_npi=pract_npi,
    identifier_system=urlify(managing_org_id),
    identifier_value=get_prov_identifier(),
    identifier_assigner='identifier_assigner', #todo
    identifier_assigner_display=managing_org_name, 
    fname=pract_item['Provider First Name'], # based on Gender
    lname=pract_item['Provider Last Name (Legal Name)'], # based on Gender
    sname=pract_item['Provider Credential Text'],
    org_npi=org_npi,
    org_name=org_name,
    location_phone=pract_item['Provider Business Practice Location Address Telephone Number']
    ))


def hcs_example(item,f_id,type,npi,hcs): # hcs= healthcareservice
    return(f_templ.healthcareservice_template.format(
    type=type,
    f_id=f_id,
    npi=npi,
    name=item['Provider Organization Name (Legal Business Name)'],
    hcs_code=spinalcase(hcs),
    HCS_Name=hcs.upper(),
    identifier_system=urlify(item['Provider Organization Name (Legal Business Name)']),
    identifier_value='{npi}-{hcs}'.format(npi=npi,hcs=spinalcase(hcs)),
    phone=item['Provider Business Practice Location Address Telephone Number'],
    service_list=get_specialty(hcs,'s_list'),
    specialty=get_specialty(hcs,'s_xml')
    # hsc_type_code,
    # hcs_type_display
    ))


def get_specialty(hcs,return_type): # hcs= healthcareservice
    specialties=[]
    specialties_xml=''
    if hcs == 'miscellaneous' and return_type=='s_list': # default value this
        return(hcs)
        
    if hcs == 'miscellaneous' and return_type=='s_xml': # default value this
        return(f_templ.hcs_specialty_template.format(
        specialty_code=hcs,
        specialty_display='Miscellaneous' 
        ))

    for k,v in nucc_healthcareservice_map.items():
        if v == hcs:
            # logging.info('hcs={hcs}, specialty={specialty} len(k) = {len}'.format(hcs=hcs,specialty=k,len=len(k)))
            if len(k) == 3: # get all the codes that begin with k
                specialties = specialties + [nucc for nucc in nucc_dict if nucc[0:3]==k]
            else:
                specialties.append(k)
    # logging.info('specialties={specialties}'.format(specialties=specialties))
    # specialties=sample(service_list,k=5) # list of five specialties
    # logging.info(random_service_list)
    if return_type=='s_list':
        return(', '.join([get_specialty_display(specialty) for specialty in specialties]))
    for specialty in specialties:
        # logging.info('hcs={hcs}, specialty={specialty}'.format(hcs=hcs,specialty=specialty))
        
        specialty_xml=f_templ.hcs_specialty_template.format(
        specialty_code=specialty,
        specialty_display=get_specialty_display(specialty)
        )
        
        specialties_xml = '{specialties_xml}{specialty_xml}'.format(specialties_xml=specialties_xml,specialty_xml=specialty_xml)
    return(specialties_xml)


def loc_example(item,f_id,type,npi):
    return(f_templ.location_template.format(
    type=type,
    f_id=f_id,
    npi=npi,
    location_identifier_system='https://{}.com'.format(spinalcase(item['Provider Organization Name (Legal Business Name)'].lower())),
    name=item['Provider Organization Name (Legal Business Name)'],
    type_code=item['Healthcare Provider Taxonomy Code_1'],
    type_code_display=get_qual_code_display(item['Healthcare Provider Taxonomy Code_1']),
    phone=item['Provider Business Practice Location Address Telephone Number'],
    address=item['Provider First Line Business Practice Location Address'], #todo add second line
    city=item['Provider Business Practice Location Address City Name'],
    state=item['Provider Business Practice Location Address State Name'],
    zip=item['Provider Business Practice Location Address Postal Code'],
    LAT=ll.lat_long[get_zip(item['Provider Business Practice Location Address Postal Code'])][0], # remove the  + 4 for looking up lat and long
    LON=ll.lat_long[get_zip(item['Provider Business Practice Location Address Postal Code'])][1],
    )
    )


def get_partof_network(id,display):
    return(f_templ.partof_org_template.format(
    partof_org_npi=spinalcase(id.lower()),
    partof_org=display
    ))


def network_example(item,f_id,type,hpid):
    return(f_templ.organization_template.format(
        type=type,
        f_id=f_id,
        npi=hpid,
        identifier_type_code='NIIP',
        identifier_type_display='National Insurance Payor Identifier (Payor)',
        identifier_type_text='The Health Plan Identifier (HPID)',
        identifier_system='https://www.qhpcertification.cms.gov/s/QHP',
        name=item['name'],
        phone=item['phone'],
        address=item['address'], #todo add second line
        city=item['city'],
        state=item['state'],
        zip=item['zip'],
        LAT=ll.lat_long[get_zip(item['zip'])][0], # remove the  + 4 for looking up lat and long
        LON=ll.lat_long[get_zip(item['zip'])][1],
        prov_type_system='http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-network-type',
        prov_type_code=item['prov_type_code'],
        prov_type_display=item['prov_type_display'],
        prov_type_text=item['prov_type_text'],
        contact_fname='Kathy',
        contact_lname="Contact",
        contactpoint_location_reference='todo',
        contactpoint_location_reference_display='todo',
        partof=get_partof_network(item['partof_id'],item['partof_display'])
        )
        )



def get_partof_org():  # return either a randomly selected managing org or empty string
    mo = choices(list(hosp_systems.keys()),[25,25,25,25])[0]
    if mo =='None':
        return('')
    else:
        return(f_templ.partof_org_template.format(
        partof_org_npi=hosp_systems[mo],
        partof_org=mo
        ))


def org_example(item,f_id,type,npi):
    return(f_templ.organization_template.format(
        type=type,
        f_id=f_id,
        npi=npi,
        identifier_type_code='NPI',
        identifier_type_display='Provider number',
        identifier_type_text='NPI',
        identifier_system='http://hl7.org/fhir/sid/us-npi',
        name=item['Provider Organization Name (Legal Business Name)'],
        phone=item['Provider Business Mailing Address Telephone Number'],
        address=item['Provider First Line Business Mailing Address'], #todo add second line
        city=item['Provider Business Mailing Address City Name'],
        state=item['Provider Business Mailing Address State Name'],
        zip=item['Provider Business Mailing Address Postal Code'],
        LAT=ll.lat_long[get_zip(item['Provider Business Mailing Address Postal Code'])][0], # remove the  + 4 for looking up lat and long
        LON=ll.lat_long[get_zip(item['Provider Business Mailing Address Postal Code'])][1],
        prov_type_system='http://terminology.hl7.org/CodeSystem/organization-type',
        prov_type_code='prov',
        prov_type_display='Healthcare Provider',
        prov_type_text='Healthcare Provider',
        contact_fname=item['Authorized Official First Name'],
        contact_lname=item['Authorized Official Last Name'],
        contactpoint_location_reference='todo',
        contactpoint_location_reference_display='todo',
        partof=get_partof_org()
        )
        )
        
def pract_example(item,f_id,type,npi):
    # use fhir xml template to create practitioner qualification instance 
    qualification = f_templ.practitioner_qual_template.format(
            license_state=item['Provider License Number State Code_1'],
            license_state_display=usps_map[item['Provider License Number State Code_1']][0],
            license_system=usps_map[item['Provider License Number State Code_1']][1],
            license_assigner=usps_map[item['Provider License Number State Code_1']][2],
            med_license=item['Provider License Number_1'],
            qual_code=item['Healthcare Provider Taxonomy Code_1'],
            qual_code_system='http://nucc.org/provider-taxonomy',
            qual_code_display=get_qual_code_display(item['Healthcare Provider Taxonomy Code_1'])
            )
            
    #  create a second  qualification instance if data is present
    if item['Provider License Number_2']:
        qualification1 = f_templ.practitioner_qual_template.format(
            license_state=item['Provider License Number State Code_2'],
            license_state_display=usps_map[item['Provider License Number State Code_2']][0],
            license_system=usps_map[item['Provider License Number State Code_2']][1],
            license_assigner=usps_map[item['Provider License Number State Code_2']][2],
            med_license=item['Provider License Number_2'],
            qual_code=item['Healthcare Provider Taxonomy Code_2'],
            qual_code_system='http://nucc.org/provider-taxonomy',
            qual_code_display=get_qual_code_display(item['Healthcare Provider Taxonomy Code_2'])
            )
        qualification = qualification + qualification1
        
    # use fhir xml template to create practitioner instance
    example = f_templ.practitioner_template.format(
        type=type,
        Type = type.capitalize(),
        f_id=f_id,
        npi=npi,
        active='true', # randomize ?
        fname=item['Provider First Name'], # based on Gender
        lname=item['Provider Last Name (Legal Name)'], # based on Gender
        sname=item['Provider Credential Text'],
        phone0=item['Provider Business Mailing Address Telephone Number'],
        phone1=get_phone1(item),
        LAT=ll.lat_long[get_zip(item['Provider Business Mailing Address Postal Code'])][0], # remove the  + 4 for looking up lat and long
        LON=ll.lat_long[get_zip(item['Provider Business Mailing Address Postal Code'])][1],
        address=item['Provider First Line Business Mailing Address'], #todo add second line
        city=item['Provider Business Mailing Address City Name'],
        state=item['Provider Business Mailing Address State Name'],
        zip=item['Provider Business Mailing Address Postal Code'],
        gender= gender[item['Provider Gender Code']],
        qualification=qualification,  # subtemplate
        communication=choices(f_templ.practitioner_comm_template,weights=[80,20])[0] # skewed random choice of en or en+es
    )
    return(example)
    

def create_entry(entries,server_path,f_id,example,Type):
    entry = f_templ.entries_templ.format(server_path=server_path, f_id=f_id, example=example, Type=Type)
    return('{entries}\n{entry}'.format(entries=entries, entry=entry))

    
    
def create_batch_bundle(entries,type):
    timestamp = '{}Z'.format(datetime.utcnow().isoformat())
    return(f_templ.batch_bundle_template.format(
    timestamp=timestamp,
    entries=entries, type=type
    ))

#****************  Main  *************************

def main(type,id_list,source=None):

    try:
        os.mkdir('{out_path}/{type}'.format(out_path=out_path,type=type))
    except FileExistsError:
        pass
    try:
        Type=rr.r_map[type]
    except KeyError:
        Type='Organization'
        
    entries = ''


    if type == 'organization':
        for item in org_list:
            npi = item['NPI']
            f_id=get_f_id(type,npi)
            logging.info('create resource id = {f_id}'.format(f_id=f_id))
            example = org_example(item,f_id,type,npi)
            id_list[type].append((npi,'{Type}/{f_id}'.format(Type=Type,f_id=f_id),item['Provider Organization Name (Legal Business Name)']))
            entries = create_entry(entries,server_path,f_id,example,Type)

    if type == 'network':
        for item in network_list:
            hpid = item['hpid']
            f_id=get_f_id(type,hpid)
            logging.info('create resource id = {f_id}'.format(f_id=f_id))
            example = network_example(item,f_id,type,hpid)
            id_list[type].append((hpid,'{Type}/{f_id}'.format(Type=Type,f_id=f_id),item['name']))
            entries = create_entry(entries,server_path,f_id,example,Type)

    elif type == 'location':
        for item in org_list:
            npi = item['NPI']
            f_id=get_f_id(type,npi)
            logging.info('create resource id = {f_id}'.format(f_id=f_id))
            example = loc_example(item,f_id,type,npi)
            id_list[type].append((npi,'{Type}/{f_id}'.format(Type=Type,f_id=f_id),item['Provider Organization Name (Legal Business Name)']))
            entries = create_entry(entries,server_path,f_id,example,Type)

            #if source == 'organization':
            #    id_list.append((f_id,item['Provider Organization Name (Legal Business Name)']))
            #elif source == 'practitioner':
            #    id_list.append((f_id,'{} {}'.format(*random_name)))
        
    elif type == 'healthcareservice':
        for item in org_list:
            npi = item['NPI']
            for service in healthcareservice_list:
                hcs_type='{hcs}-{type}'.format(type=type,hcs=spinalcase(service[0:27]))
                f_id=get_f_id(hcs_type,npi)
                logging.info('create resource id = {f_id}'.format(f_id=f_id))
                example = hcs_example(item,f_id,type,npi,service)
                id_list[type].append((npi,'{Type}/{f_id}'.format(Type=Type,f_id=f_id),'{name} {Service} Service'.format(name=item['Provider Organization Name (Legal Business Name)'],Service=titlecase(service))))
                entries = create_entry(entries,server_path,f_id,example,Type)

    elif type == 'practitioner':
        skip_list=[]
        for item in pract_list:
            npi = item['NPI']
            f_id=get_f_id(type,npi)
            logging.info('create resource id = {f_id}'.format(f_id=f_id))
            try:
                example = pract_example(item,f_id,type,npi)
                id_list[type].append((npi,'{Type}/{f_id}'.format(Type=Type,f_id=f_id),'{fname} {lname}'.format(fname=item['Provider First Name'],lname=item['Provider Last Name (Legal Name)'])))
                entries = create_entry(entries,server_path,f_id,example,Type)
            except KeyError as e:
                logging.error('practitioner {npi} skipped because of {e}'.format(npi=npi,e=e))
                skip_list.append(npi)
        
    elif type == 'practitionerrole': # one or more for each practitioner need to assign to org
        for item in pract_list:
            org_npi_list=[]
            pract_npi = item['NPI']
            # assign pract to org and network
            org_item_list=get_org(item['Provider Business Practice Location Address State Name'],item['Provider Business Practice Location Address Postal Code']) # get lst of org item jsut one for now
            #logging.info('org_item_list ={}',format(org_item_list))
            network_item_list=get_network(item['Provider Business Practice Location Address State Name'])
            for i,org_item in enumerate(org_item_list + network_item_list):
                f_id=get_f_id(type,'{pract_npi}-{i}'.format(pract_npi=pract_npi,i=i))
                logging.info('create resource id = {f_id}'.format(f_id=f_id))
                try:
                    org_npi = org_item['NPI']
                    org_name = org_item['Provider Organization Name (Legal Business Name)']
                    example = practrole_example(item,f_id,type,pract_npi,org_npi,org_name)
                except KeyError: #network
                    org_npi = org_item['hpid']
                    org_name = org_item['name']
                    managing_org_id = org_item['partof_id']
                    managing_org_name = org_item['partof_display']
                    example = practrole_network_example(item,f_id,type,pract_npi,org_npi,org_name,managing_org_id,managing_org_name)
                org_npi_list.append(org_npi)
                id_list[type].append((pract_npi,'{Type}/{f_id}'.format(Type=Type,f_id=f_id),'{fname} {lname}'.format(fname=item['Provider First Name'],lname=item['Provider Last Name (Legal Name)']),org_npi))
                entries = create_entry(entries,server_path,f_id,example,Type)

    elif type == 'organizationrole': # one  for each org and network assigned to org assign all networks for now
        for item in org_list:
            network_npi_list=[]
            org_npi = item['NPI']
            # assign org to network
            network_item_list=get_network(item['Provider Business Practice Location Address State Name'],True)
            for i,network_item in enumerate(network_item_list):
                f_id=get_f_id(type,'{org_npi}-{i}'.format(org_npi=org_npi,i=i))
                logging.info('create resource id = {f_id}'.format(f_id=f_id))
                network_npi = network_item['hpid']
                network_name = network_item['name']
                managing_org_id = network_item['partof_id']
                managing_org_name = network_item['partof_display']
                example = orgrole_example(item,f_id,type,network_npi,network_name,managing_org_id,managing_org_name)
                network_npi_list.append(network_npi)
                id_list[type].append((org_npi,'{Type}/{f_id}'.format(Type=Type,f_id=f_id),'{name} Network Member'.format(name=item['Provider Organization Name (Legal Business Name)']),network_npi))
                entries = create_entry(entries,server_path,f_id,example,Type)

 

    logging.info('create {type} example: \n{example}'.format(type=type,example=f_id))  # change example to f_id for faster perfomance
        
        
    batch_bundle = create_batch_bundle(entries,type)
    


    write_xml(out_path,type,batch_bundle,source)  #save to file

    return()
    
#********************* __name__ == "__main__" ********************

#This only happens when this module is called directly:
if __name__ == "__main__":
    resource_keys = dict(  # create a map of resource_ids to create a relational table
        practitioner=[],
        organization=[],
        network=[],
        location=[],
        healthcareservice=[],
        practitionerrole=[],
        organizationrole=[]
        )
        
    main('organization',resource_keys)
    main('network',resource_keys)
    main('location',resource_keys,'organization')
    main('healthcareservice',resource_keys,'organization')
    main('practitioner',resource_keys)
    main('practitionerrole',resource_keys,'practitioner')
    main('organizationrole',resource_keys,'organization')
    

    #main('location',resource_keys['location'],'practitioner')

        
    for k,v in resource_keys.items(): # convert to csv:
        write_resource_csv(k,v)
        #pairs = [str([*t]) for t in resource_keys[type]]
        #print(pairs)
        #logging.info('{} resource_keys:\n {}'.format(type.capitalize(),resource_keys[type]))

    logging.debug('end of program')
