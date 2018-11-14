#!/usr/bin/python

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
)

'''


import csv
from pprint import pprint


my_file = 'synthea/src/main/resources/providers/hospitals.csv'
org_type = my_file.split('.')[0].split('/')[-1]

with open(my_file) as f:
   my_list = [i for i in csv.DictReader(f,fieldnames=None, restkey='id', restval=None, dialect='excel')]

pprint(my_list[0:10])
#make npi as 999 + id padded with leading zero to make length equal TODO validate to validate with Luhn algorithm

#for each create append a kv pair for npi and org-type
for item in my_list:
    item['npi'] = '999{}'.format(item[''].zfill(7))
    item['org-type'] = org_type

pprint(my_list[0:10])
   
# create VHDIR FHIR resources instances using this data