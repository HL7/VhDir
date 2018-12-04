import csv
from pprint import pprint, pformat
from datetime import datetime
import os, sys, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

# in_path ='/Users/ehaas/Downloads/'
#in_path ='/Users/ehaas/Documents/FHIR/VhDir/synthea/src/main/resources/providers'
in_path = '/Volumes/Laptop_Backup/NPPES/CROSSWALK_MEDICARE_PROVIDER_SUPPLIER_to_HEALTHCARE_PROVIDER_TAXONOMY.csv'

def get_taxonomy():
    with open('{in_path}'.format(in_path=in_path)) as f:
        for line in csv.DictReader(f, fieldnames=None, restkey='id', restval=None, dialect='excel'):
            print("'{}': '{}',".format(line['PROVIDER TAXONOMY CODE'],line['PROVIDER TAXONOMY DESCRIPTION']))
    return()
    
#This only happens when this module is called directly:
if __name__ == "__main__":
    get_taxonomy()


