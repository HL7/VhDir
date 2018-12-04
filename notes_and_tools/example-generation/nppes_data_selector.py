# ===================================
# create VHDIR FHIR resources instances using this data
# run in python 3.5 or above
# ====================================


# open nnpess csv and read one line at at time to get Max records.abs and save as csv

import csv
from pprint import pprint, pformat
from datetime import datetime
import nppes_fieldnames as fn
import os, sys, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

# in_path ='/Users/ehaas/Downloads/'
#in_path ='/Users/ehaas/Documents/FHIR/VhDir/synthea/src/main/resources/providers'
in_path = '/Volumes/Laptop_Backup/NPPES'
out_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/sample-nppes-data'
server_path = 'http://test.fhir.org/r4'
nppes_file = 'npidata_pfile_20050523-20181111'
nppes_endpoint_file = 'endpoint_pfile_20050523-20181111'
states = ['MA','CT','RI']
allowed_org_codes = ('261Q','282N','2865','302','305','273','284','261Q')
# hospitals etc



def get_nppes(type,max):
    count = 0
    files = []
    with open('{in_path}/{nppes_file}.csv'.format(in_path=in_path,nppes_file=nppes_file)) as f:
        for i,line in enumerate(csv.DictReader(f, fieldnames=None, restkey='id', restval=None, dialect='excel')):

            if line['Entity Type Code'] == type and line['Provider Business Practice Location Address State Name'] in states and (type != '2' or line['Healthcare Provider Taxonomy Code_1'].startswith(allowed_org_codes)):
              print(count,i,line['Entity Type Code'],line['Provider Business Practice Location Address State Name'],line['Healthcare Provider Taxonomy Code_1'])
              files.append(line)
              count += 1
            if count >= max:
                return(files)



def get_nppes_endpoints(npi):
    print('endpoint npi ={}'.format(npi))
    with open('{in_path}/{nppes_endpoint_file}.csv'.format(in_path=in_path,nppes_endpoint_file=nppes_endpoint_file)) as f:
        for line in csv.DictReader(f, fieldnames=None, restkey='id', restval=None, dialect='excel'):
            print(npi, line['NPI'],line['Endpoint'])
            if line['NPI'] == npi :
              return(line)
    return()


def write_nppes_data(file_name,data):
    with open('{out_path}/sample-nppes-{file_name}-data.csv'.format(out_path=out_path,file_name=file_name), mode='w', newline='') as csv_file:
        fieldnames = fn.fieldnames
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, dialect='excel', quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for line in data:
            print('writing .... {} npi = {}'.format(file_name, line["NPI"]))
            writer.writerow(line)

        
        
#This only happens when this module is called directly:
if __name__ == "__main__":
    endpoints =[]
    practitioners = get_nppes('1',20)  # 'Entity Type Code'] == '1' for practitioners,  max records = 2000
    for i,item in enumerate(practitioners):
        print('practitioner{} npi = {}'.format(i, item["NPI"]))
        # get_nppes_endpoints(item["NPI"])  # is empty :-(
        write_nppes_data('practitioner',practitioners)  # write to new file
        
    organizations = get_nppes('2',40)  # 'Entity Type Code'] == '2' for organizations,  max records = 20
    for i,item in enumerate(organizations):
        print('organization{} npi = {}'.format(i, item["NPI"]))
    write_nppes_data('organization',organizations)  # write to new file

        
        
        
        
logging.debug('end of program')