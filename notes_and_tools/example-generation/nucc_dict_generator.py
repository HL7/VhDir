# ===================================
# create a dict from the nucc csv file
# ====================================


# open nucc csv and read one line at at time to get Max records.abs and save as csv

import csv
from pprint import pprint, pformat
from datetime import datetime
import os, sys, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

# in_path ='/Users/ehaas/Downloads/'
#in_path ='/Users/ehaas/Documents/FHIR/VhDir/synthea/src/main/resources/providers'
in_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/nucc_taxonomy.csv'
out_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation'
out_file = 'nucc_dict.py'
specialty_codesystem ='http://hl7.org/fhir/ValueSet/c80-practice-codes'
server_path = 'http://test.fhir.org/r4'

def get_nucc():
    nucc_dict = {}
    nucc_groups = []
    with open('{in_path}'.format(in_path=in_path)) as f:
        fieldnames = ['Code', 'Grouping', 'Classification', 'Specialization', 'Definition', 'Notes']
        next(csv.DictReader(f, fieldnames=fieldnames), None)  # skip the headers
        for line in csv.DictReader(f, fieldnames=fieldnames):
            k=line['Code']
            logging.info('code = {k} grouping = {grouping}, category = {category}, specialty = {specialty}'.format(k=k,grouping=line['Grouping'],category=line['Classification'],specialty=line['Specialization']))
            
            nucc_groups.append(line['Grouping']) # get nucc groups
            v=tuple(v for v in line.values())
            
            logging.info('creating nucc_dict k = {k} v = {v}'.format(k=k,v=v))
            nucc_dict[k]=v
            
    return(nucc_dict)
            
            
def get_nucc_role(nucc_dict):
    nucc_role_map={}
    for i in nucc_dict:
        k=i
        r=[(j,nucc_dict[j][1]) for j in nucc_dict if j == '{k}00000X'.format(k=k[0:4])]
        try:
           logging.info('Map to NUCC highlevel roles using 1st four characters code = {k} NUCC highlevel roles (PR.code) = {r}'.format(k=k,r=r[0]))
           nucc_role_map[k]=r[0],
        except IndexError:
           logging.info('Map to NUCC highlevel roles using 1st four characters code = {k} NUCC highlevel roles (** IS SAME CODE **) (PR.code) = {r}'.format(k=k,r=nucc_dict[k][1]))
           nucc_role_map[k]=(nucc_dict[k][1])
    return(nucc_role_map)



def get_nucc_specialty(nucc_dict):
    for i in nucc_dict:
        k=i
        s1=nucc_dict[i][2]
        s2=nucc_dict[i][3]
        
        if s2:
            logging.info('Map to NUCC specialty  code = {k} NUCC specialty = {s}'.format(k=k,s=s2))
        elif s1:
            logging.info('Map to NUCC specialty  code = {k} NUCC specialty = {s}'.format(k=k,s=s1))
        else:
            logging.info('Map to NUCC specialty  code = {k} NUCC specialty = {s}'.format(k=k,s='general practice'))

    return()


def get_nucc_hcs(nucc_dict):        # for creating a Healthcare Service list 
    for i in nucc_dict:
        k=i
        s=nucc_dict[i][2]
        t=nucc_dict[i][3]
        

        print('{k}'.format(k=k,s=s.lower(), t=t.lower()))
        # except IndexError:
        #  logging.info('Map to NUCC highlevel roles using 1st four characters code = {k} NUCC highlevel roles (** IS SAME CODE **) (PR.code) = {r}'.format(k=k,r=nucc_dict[k][1]))



# TODO lookup the snomed equivalent





#This only happens when this module is called directly:

if __name__ == "__main__":
    endpoints =[]
    nucc_dict = get_nucc()
    #with open('{out_path}/{out_file}'.format(out_path=out_path,out_file=out_file),'w') as fout:
    #    fout.write(pformat(nucc_dict, width=1000))
    print('nucc_role_map =')
    pprint(get_nucc_role(nucc_dict),width=200)
    # get_nucc_specialty(nucc_dict)
    # get_nucc_hcs(nucc_dict)
        
        
logging.debug('end of program')