# start atom from venv Flask36
# FHIR R4 models 'fhirr4models' package in /Users/ehaas/Documents/Python/Venv/Flask36/lib/python3.6/site-packages
import fhirr4models.structuredefinition as sd
import fhirr4models.elementdefinition as ed

from fhirr4models.fhirabstractbase import FHIRValidationError
import json, yaml, isodate
from pprint import pprint
import sys
# print(sys.path)

ignore_elements = ['id','meta','implicitRules','language','text']

# in_path ='/Users/ehaas/Downloads/'
in_path ='/Users/ehaas/Documents/FHIR/VhDir/output'
#in_path = '/Users/ehaas/Documents/FHIR/VhDir/source/pre_mustsupport_profiles'
out_path = '/Users/ehaas/Documents/FHIR/VhDir/source/mustsupport_profiles'
#profile_list = ['StructureDefinition-vhdir-practitioner']


profile_list = ['StructureDefinition-vhdir-careteam',
'StructureDefinition-vhdir-endpoint',
'StructureDefinition-vhdir-healthcareservice',
'StructureDefinition-vhdir-insuranceplan',
'StructureDefinition-vhdir-location',
'StructureDefinition-vhdir-network',
'StructureDefinition-vhdir-organization',
'StructureDefinition-vhdir-organizationaffiliation',
'StructureDefinition-vhdir-practitioner'
'StructureDefinition-vhdir-practitionerrole',
'StructureDefinition-vhdir-restriction',
'StructureDefinition-vhdir-validation']


extension_list = ['StructureDefinition-accessibility',
'StructureDefinition-careteam-alias',
'StructureDefinition-communication-proficiency',
'StructureDefinition-contactpoint-availabletime',
'StructureDefinition-contactpoint-viaintermediary',
'StructureDefinition-digitalcertificate',
'StructureDefinition-ehr',
'StructureDefinition-endpoint-rank',
'StructureDefinition-endpoint-reference',
'StructureDefinition-endpoint-usecase',
'StructureDefinition-healthcareservice-reference',
'StructureDefinition-identifier-status',
'StructureDefinition-insuranceplan-reference',
'StructureDefinition-location-reference',
'StructureDefinition-network-reference',
'StructureDefinition-newpatientprofile',
'StructureDefinition-newpatients',
'StructureDefinition-org-alias-period',
'StructureDefinition-org-alias-type',
'StructureDefinition-org-description',
'StructureDefinition-practitioner-qualification',
'StructureDefinition-qualification',
'StructureDefinition-usage-restriction'
]

def get_rjson(file):  # get json file from path and return as dict
    with open('{in_path}/{file}.json'.format(in_path=in_path,file=file), 'r') as rjson:
        return(json.load(rjson))
        
def put_rjson(rinst,fname):  # upload fhir model instance as json to path
    with open('{out_path}/{fname}.json'.format(out_path=out_path, fname=fname), 'w') as fjson:
        fjson.write(json.dumps(profile.as_json(), sort_keys=True, indent=4))
    return()


def put_ryml(rinst,fname):  # upload fhir model instance as yml to path
    with open('{out_path}/{fname}.yml'.format(out_path=out_path, fname=fname), 'w') as fyml:
        write.fyml(yaml.dump(rinst, default_flow_style=False))
    return()

def get_ryml(file):  # get yml file from path and return as dict
    with open('{out_path}/{file}.yml'.format(out_path=out_path,file=file), 'r') as ryml:
        return(json.load(ryml))


def create_new_diff_list(old_diff_list): # generated white lists of elements using snapshot element ids

    # blacklist of elements to ignore
    ignore_elements = ['id','meta','implicitRules','language','text','contained']
    ignore_me_too = ['id','url','modifierExtension']
    ignore_extension_list = []
    new_diff_list = []

    for elem in profile.snapshot.element[1:]: #skip root
        element_id = elem.id
        print('element_id = {}'.format(element_id))
        element_id_list = element_id.split('.')
        #print('element_id_list = {}'.format(element_id_list))

        not_extension_element = not any(':' in s for s in element_id_list[0:-1])
        # print('element_id_list minus 1  = {} check for : = {}'.format(element_id_list[0:-1],not_extension_element))
        element_id_firstdot = element_id_list[1]
        element_id_lastdot = element_id_list[-1]

        # print('element_id = {} : found = {}'.format(element_id, element_id_lastdot.find(':')))

        if element_id_firstdot not in ignore_elements and element_id_lastdot not in ignore_me_too and not_extension_element : # remove all inherited stuff
            #print(element_id)
            new_diff_list.append(element_id)
    return(new_diff_list)



def process_diff(old_diff_list, new_diff_list): # use generated list to process diff

    exclude_mustsupport_list = ['extension', 'modifierExtension']

    for new_element_id in new_diff_list:
            
            #print('new_element_id = {}'.format(new_element_id))
            new_element_id_list = new_element_id.split('.')
            #print('new_element_id_list = {}'.format(new_element_id_list))

            new_element_id_firstdot = new_element_id_list[1]
            new_element_id_lastdot = new_element_id_list[-1]
            add_mustSupport = [i for i,elem in enumerate(old_diff_list) if elem.id == new_element_id]
            if add_mustSupport:
                element_index = add_mustSupport[0]
                print('in = {}'.format(new_element_id))
                print('new_element_id_lastdot = {}'.format(new_element_id_lastdot))
                if new_element_id_lastdot in exclude_mustsupport_list:
                    print('add mustSupport = False to {}'.format(element_index))
                    profile.differential.element[element_index].mustSupport = False
                else:
                    print('add mustSupport = True to {}'.format(element_index))
                    profile.differential.element[element_index].mustSupport = True
            elif new_element_id_lastdot not in exclude_mustsupport_list:
                new_element = ed.ElementDefinition(dict(id=new_element_id,path=new_element_id,mustSupport=True))
                print('out = {}'.format(new_element_id))
                try:
                    element_index = element_index + 1  # increment the element index if multiple new elements
                    print('*** element_index = {}, element.id = {}'.format(element_index,profile.differential.element[element_index].id))
                    old_diff_list.insert(element_index, new_element)
                except UnboundLocalError:
                    print ('===========skip element = {new_element_id} ================='.format(new_element_id=new_element_id))
                except IndexError:
                    old_diff_list.append(new_element)
        
                # print('old_diff_list ={}'.format(old_diff_list))
    return()


def remove_elements():  # remove unwanted elements from the Source
    print('===========remove elements=============')
    del_elements= ['meta','text','version','mapping','snapshot']
    for del_element in del_elements:
        print(del_element, type(del_element))
        setattr(profile, del_element, None)   
    print("profile.differential.element length={}".format(len(profile.differential.element)))
    try:
        temp_diff_list = [item for item in profile.differential.element[1:] if item.id.split('.')[1] not in (del_elements + ['id'])]
        print("temp_diff_list length ={}".format(len(temp_diff_list)))
    except IndexError:
        pass
    #temp_diff_list = temp_diff_list.insert(0,profile.differential.element[0]) 
        
    setattr(profile.differential, 'element', [profile.differential.element[0]] + temp_diff_list )


    # print(json.dumps(profile.differential.as_json(),indent=4))
    return()

def main():  # add must supports to all elements and recreate a different

    old_diff_list = profile.differential.element # copy of sd.diff

    new_diff_list= create_new_diff_list(old_diff_list)

    process_diff(old_diff_list, new_diff_list)

    # print(json.dumps(profile.as_json(), sort_keys=True, indent=4))

    remove_elements() # remove unwanted elements from the Source

    # save to out_path
    fjson_name = 'structuredefinition-profile-{profile_id}'.format(profile_id=profile.id) # for profiles
    #fjson_name = 'structuredefinition-ext-{profile_id}'.format(profile_id=profile.id) # for extensions
    
    put_rjson(profile,fjson_name)
    return()

for fname in profile_list:
#for fname in extension_list:
    fhirdict = get_rjson(fname)
    try:
        profile = sd.StructureDefinition(fhirdict)
        r_type = profile.snapshot.element[0].id
        print(r_type)
        if __name__ == '__main__':
            main()
    except FHIRValidationError as e:
        print ('==================type={fname} will not load into model============'.format(fname=fname))
        print(e)

print('done')
     
     
      
     
     
     
     
     
     
     
     
     
    


