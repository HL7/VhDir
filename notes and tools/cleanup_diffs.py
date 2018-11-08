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
#in_path ='/Users/ehaas/Documents/FHIR/VhDir/output'
in_path = '/Users/ehaas/Documents/FHIR/VhDir/source/resources'
out_path = '/Users/ehaas/Documents/FHIR/VhDir/source/mustsupport_profiles'
# fname = 'StructureDefinition-vhdir-practitioner'

profile_list = [
'structuredefinition-ext-accessibility',
'structuredefinition-ext-careteam-alias',
'structuredefinition-ext-communication-proficiency',
'structuredefinition-ext-contactpoint-availabletime',
'structuredefinition-ext-contactpoint-viaintermediary',
'structuredefinition-ext-digitalcertificate',
'structuredefinition-ext-ehr',
'structuredefinition-ext-endpoint-rank',
'structuredefinition-ext-endpoint-reference',
'structuredefinition-ext-endpoint-usecase',
'structuredefinition-ext-healthcareservice-reference',
'structuredefinition-ext-identifier-status',
'structuredefinition-ext-insuranceplan-reference',
'structuredefinition-ext-location-reference',
'structuredefinition-ext-network-reference',
'structuredefinition-ext-newpatientprofile',
'structuredefinition-ext-newpatients',
'structuredefinition-ext-org-alias-period',
'structuredefinition-ext-org-alias-type',
'structuredefinition-ext-org-description',
'structuredefinition-ext-practitioner-qualification',
'structuredefinition-ext-qualification',
'structuredefinition-ext-usage-restriction',
'structuredefinition-profile-vhdir-careteam',
'structuredefinition-profile-vhdir-endpoint',
'structuredefinition-profile-vhdir-healthcareservice',
'structuredefinition-profile-vhdir-insuranceplan',
'structuredefinition-profile-vhdir-location',
'structuredefinition-profile-vhdir-network',
'structuredefinition-profile-vhdir-organization',
'structuredefinition-profile-vhdir-organizationaffiliation',
'structuredefinition-profile-vhdir-practitioner',
'structuredefinition-profile-vhdir-practitionerrole',
'structuredefinition-profile-vhdir-restriction',
'structuredefinition-profile-vhdir-validation'
]

def get_rjson(fname):  # get json file from path and return as dict
    with open('{in_path}/{fname}.json'.format(in_path=in_path, fname=fname)) as rjson:
        return(json.load(rjson))
    
        
def put_rjson(fname):  # upload fhir model instance as json to path
    with open('{out_path}/{fname}.json'.format(out_path=out_path, fname=fname), 'w') as fjson:
        fjson.write(json.dumps(profile.as_json(), sort_keys=True, indent=4))
    return()


def remove_elements():
    pass


def main():  # add must supports to all elements and recreate a different

    remove_me = ['id','meta','implicitRules','language','text','contained']
    remove_me2 = ['extension','modifierExtension']
    remove_me_list = []
    for i, elem in enumerate(profile.differential.element[1:]): #skip root

        element_id = elem.id
        element_id_list = element_id.split('.')
        element_id_firstdot = element_id_list[1]
        element_id_lastdot = element_id_list[-1]
        #print('element_id = {},'.format(element_id))
        try:
            next_element_id = profile.differential.element[i + 2].id  # remember skipped the root
            next_element_id_list = next_element_id.split('.')
            next_element_id_firstdot = next_element_id_list[1]
            next_element_id_lastdot = next_element_id_list[-1]
            #print('next_element_id = {},'.format(next_element_id))
        except IndexError:
            pass

        if element_id_firstdot in remove_me or (element_id_lastdot in remove_me2 and ':' not in next_element_id_lastdot): # create a index list of unwanted stuff
            print('i = {} element_id = {},'.format(i, element_id), element_id_firstdot, element_id_lastdot,' i+2 = {} next_element_id = {},'.format(i + 2,next_element_id), next_element_id_lastdot)
            remove_me_list.append(i)

    print('remove_me_list = {}'.format(remove_me_list))

    remove_elements() # remove unwanted elements from the Source
    return()

for fname in profile_list:
#for fname in extension_list:
    fhirdict = get_rjson(fname)
    try:
        profile = sd.StructureDefinition(fhirdict)
        #r_type = profile.snapshot.element[0].id
        print(profile.title)
        if __name__ == '__main__':
            main()
    except FHIRValidationError:
        print ('==================type={fname} will not load into model============'.format(fname=fname))
    # save to out_path
    #fjson_name = 'structuredefinition-profile-{profile_id}'.format(profile_id=profile.id) # for profiles
    #fjson_name = 'structuredefinition-ext-{profile_id}'.format(profile_id=profile.id) # for extensions
    put_rjson(fname)

print('done')
     
     
      
     
     
     
     
     
     
     
     
     
    


