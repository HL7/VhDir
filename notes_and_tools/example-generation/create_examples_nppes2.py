# ===================================
# create VHDIR FHIR resources instances using the the subset of the nppes data files:
# run in python 3.6 or above
# see requirements.txt for modules
# this set of examples is produced using fstrings in json and validated using the python-client models
# ====================================

import fhir_example_templates2 as f_templ
import base64_geosjon as b64
import rR_dict as rr
import name_generator as names
import taxonomy_codes as t
import csv
from json import dumps, loads, load, dump
from datetime import datetime
from stringcase import spinalcase, titlecase, snakecase
from fhirr4models import bundle as B
from fhirr4models import practitioner as P
from fhirr4models import organization as O
from fhirr4models import organizationaffiliation as OA
from fhirr4models import practitionerrole as PR
from fhirr4models import endpoint as EP
from fhirr4models import location as L
from requests import put,get,post
from xml.etree import ElementTree




from pprint import pformat, pprint

import os, sys, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

#***********Globals******************

timestamp = f'{datetime.utcnow().isoformat()}Z'


in_path ='/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/sample-nppes-data'
out_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples'
server_path = 'http://vhdir-demo.fhir.org/fhir'
convert_server = 'http://wildfhir.aegis.net/fhir3-5-0'

x_headers ={
'Content-Type':'application/fhir+xml',
'Accept':'application/fhir+xml'
}

j_headers ={
'Content-Type':'application/fhir+json',
'Accept':'application/fhir+json'
}


out_folders = ['','20181206-small/','20181206-large/']

states = ['Massachusetts','Connecticut','Rhode Island', 'Greater Boston Area', 'Greater Hartford Area']

addins = {'addin-org-role': ('organizationrole', 'org_roles') ,
            'addin-pract-role': ('practitionerrole', 'pract_roles')}  # addin_type name: merged with type

addin_networks = {
'State of Massachusetts Preferred Provider Network' : ('ma-gic-ppo','MA'),
'State of Connecticut HMO' : ('ct-hmo','CT'),
'State of Rhode Island Preferred Provider Network' : ('ri-ppo','RI'),
'United Technologies Preferred Provider Network' : ('ut-ppo','Greater Hartford Area')}


example_files = dict(
orgs = '20181206-large/organization/vhdr-organization-example-bundle',
pract_roles = '20181206-large/practitionerrole/vhdr-practitionerrole-example-bundle',
managing_orgs = '20181206-large/managing-org/vhdr-organization-managing-org-example-bundle',
pract0 = '20181206-large/practitioner/vhdir-p-examples-bundle-8b0a8971f1074899b16f98a9bad4db46',
pract1 = '20181206-large/practitioner/vhdir-p-examples-bundle-8f96a18cda224768b205c2bdc18384fa',
pract2 = '20181206-large/practitioner/vhdir-p-examples-bundle-a74ccd6f7c3c4e83b63f1a42c64459b2',
pract3 = '20181206-large/practitioner/vhdir-p-examples-bundle-bc873f18d760417ab9ae1900804460ed',
hie_org_roles = '20181206-large/hie-orgaffiliation/vhdr-organizationaffiliation-hie-orgaffiliation-example-bundle',
hc_services = '20181206-large/healthcareservice/vhdr-organization-healthcareservice-example-bundle',
networks ='20181206-large/network/vhdr-network-example-bundle',
org_roles = '20181206-large/organizationrole/vhdr-organizationrole-example-bundle',
locations = '20181206-large/location/vhdr-organization-location-example-bundle',
endpoints = '20181206-large/endpoint/vhdr-endpoint-example-bundle',
insuranceplans = '20181206-large/insuranceplan/vhdr-insuranceplan-example-bundle',
)

western_ma_zips = ['01101','01152','01144','01103','01102','01111','01115','01138','01139','01199','01105','01090','01107','01104','01089','01109','01108','01001','01014','01021','01013','01118','01106','01119','01030','01116','01020','01151','01129','01128','01028','01022','01041','01086','01040','06078','06080','06082','01095','06083','01056','01036','01085','01077','06093','06072','01075','01073','06071','01033','01080','06096','06026','01071','06016','06088','01027','06035','06064','01009','01057','06060','01097','01063','01079','01061','01007','01060','01069','01062','06081','06029','06090','06095','01035','06006','06027','06028','06075','01034','01053','06074','06002','01004','01059','06077','01081','01008','01050','01038','06076','06084','01088','06066','06070','01002','01003','01010','06059','01092','06091','01082','06092','01066','01012','06042','01083','01039','06104','06199','06089','06120','01521','06020','06112','06128','06101','06279','01011','06108','06063','06065','06265','06041','06045','01093','06019','06105','01029','06115','01585','06152','06103','06183','06040','06123','06126','06127','06129','06131','06132','06134','06140','06141','06142','06143','06144','06145','06146','06147','06150','06151','06153','06154','06155','06156','06160','06161','06167','06176','06180','06117','06138','01084','01096','06102','06119','06118','06061','01518','06043','01373','01375','06133','06106','06001','06114','06107','06251','01506','01054','01253','01072','01355','06238','01098','01566','01243','06110','06022','01255','01032','06021','01031','06278','06269','06098','06057','01037','06268','06033','01531','06232','01026','06109','01341','06025','01550','01535','06032','06085','01094','01515','06030','06034','06242','06282','06111','01342','06250','06013','06053','06248','01366','01244','01508','01351','01330','06094','01245','01223','06067','01347','06051','01235','06281','01264','06073','01074','01509','01507','06050','01379','06237','06235','06058','01562','06062','06052','06790','01068','01259','01349','06244','01070','06447','06792','01005','01302','01238','01376','06262','06791','01571','06010','06226','06245','01338','06256','06023','06416','06230','06267','01380','06231','01370','06011','06480','06259','06258','01542','06024','01344','06037','06247','01524','06781','06018','01301','01270','01537','01260','06255','06280','01242','01612','01222','01354','06246','06266','06756','06414','06786','06474','06489','06249','01543','01230','01331','06778','01226','06456','01611','06459','06031','06264','01540','06424','06457','06782','01570','01227','01364','06137','01240','06277','01501','01339','01263','01257','01360','01262','06479','01603','06234','01452','06481','01256','06263','06759','01340','06716','01229','01602','06260','06787','06467','06450','01337','01346','01468','01202','01203','06415','06451','01378','06233','01586','06254','06455','01520','01609','01224','06444','06796','01610','06241','01522','01236','06753','06330','06469','01266','06336','01225','01608','06350','01601','01613','01614','01615','01653','01655','06331','01607','01527','06704','06068','06763','01343','01438','01605','01436','06750','06795','06079','06779','06387','01590','01201','06705','01516','01606','06710','01252','01541','01526','01254','01604','06039','06332','01368','06702','06239','06334','01367','01258','06441','06410','06701','06703','06720','06721','06722','06723','06724','06725','06726','06749','06758','06243','01441','06422','06408','06411','01220','06423','06754','06389','06438','06706','06751','06383','06708','01583','01237','06374','01440','06495','02859','06420','06492','06712','12017','06069','06494','06493','06360','05354','01350','06380','05358','12517','01545','01473','01546','01536','01560','12029','02824','06777','01519','01475','06354','05342','03451','01247','01588','01564','06377','06762','06439','01505','06793','03441','12165','06794','12125','06770','02814','06412','01525','05361','03470','06798','06370','01534','01569','01538','12516','12529','06351','02858','12546','02830','01267','06518','02826','06757','12060','06382','06419','06373','02839','12168','06353','12503','01510','01568','06472','03447','01453','06524','02825','06365','01430','12037','12195','06417','05302','05303','05304','01532','05350','06473','05344','01581','06403','01561','01420','05301','06785','02876','06783','01529','06443','02857','06442','12040','02827','06409','01503','05352','06437','02815','06426','06371','12501','02829','06384','12169','06335','06333','06514','01784','06471','12136','01523','12075','01756','12022','12592','03469','03446','12521','12502','12565','03465','06375','01747','06517','06478','03461','03443','03466','12024','12062','02896','01504','06488','05363','01757','06338','12567','06339','01748','06776','03462','01431','06487','12530','06755','06498','06349','01740','12544','01462','02828','06413','01772','01467','06525','06483','01752','05261','06513','06385','06752','06475','02917','05357','12115','02895','06515','02816','12513','03452','06357','02831','06359','06511','01749','01745','06501','06502','06503','06505','06506','06507','06508','06509','06520','06521','06530','06531','06532','06533','06534','06535','06536','06537','06538','06540','06510','06405','02019','05362','12581','12594','06401','03071','12184','06784','06504','05351','02817','12153','06320','06491','12506','12522','06512','01434','01474','01451','12132','02838','12138','12123','01464','02919','06376','02873','06519','01721','06482','12534','06340','12130','06418','05341','03435','03455','05260','01746','01469','02802','12523','06372','12018','02823','12172','12545','12106','06804','06355','02053','01472','01775','01702','12174','02911','02921','06516','03467','12541','02833','03444','02864','02865','06440','02038','12050','06484','02832','06378','06388','01719','01432','06477','06404','12063','01701','06470','12514','01703','01704','01705','03048','02070','05356','02822','05201','06468','02904']

hartford_zips = ['06101','06120','06199','06104','06115','06103','06152','06183','06123','06126','06127','06129','06131','06132','06134','06140','06141','06142','06143','06144','06145','06146','06147','06150','06151','06153','06154','06155','06156','06160','06161','06167','06176','06180','06112','06105','06108','06102','06128','06138','06106','06114','06133','06118','06119','06006','06117','06110','06107','06028','06095','06074','06109','06002','06042','06041','06045','06040','06111','06033','06064','06067','06025','06088','06089','06053','06032','06096','06051','06030','06034','06001','06070','06081','06016','06050','06073','06066','06052','06092','06026','06043','06085','06023','06416','06062','06480','06037','06020','06083','06080','06019','06035','06078','06447','06022','06248','06082','06029','06093','06232','06013']

boston_zips = ['02018','02043','01718','01719','01720','02134','01913','02474','02475','02476','02475','01431','01721','02339','02466','02322','01432','01434','02457','01815','02211','02212','02241','02151','01730','01731','02019','02478','02479','02779','01503','01915','01915','01504','01740','02108','02109','02110','02111','02112','02113','02114','02115','02116','02117','02118','02119','02120','02121','02122','02123','02124','02125','02126','02127','02128','02129','02130','02131','02132','02133','02134','02135','02136','02137','02163','02196','02199','02201','02203','02204','02205','02206','02210','02211','02212','02215','02217','02222','02228','02241','02266','02283','02284','02293','02295','02297','02298','02201','02467','02467','02266','02215','01719','01719','02184','02185','02184','02184','02185','02020','02135','02445','02446','02447','02467','02447','01803','01805','01922','02138','02139','02140','02141','02142','02163','02238','02139','02021','01741','02330','02355','02366','02297','02360','02783','02129','02712','02150','02493','02467','01778','02025','01742','01923','02026','02027','01432','01434','02715','02121','02122','02124','02125','02124','02124','02030','02331','02332','02474','01504','02128','02228','02184','02141','02355','01904','02031','02186','02359','02143','02718','02032','02538','02472','02189','01929','02149','01745','02293','02477','02241','01432','02035','02035','01701','01702','01703','01704','01705','01701','01701','02038','01910','01930','01931','02041','02040','02121','01936','01982','02339','02340','01731','01451','02238','02238','02493','01937','02018','02043','02044','02343','01746','01747','01748','02169','01749','02045','02047','02126','02136','02137','02139','01938','02090','02130','02295','02217','02493','02142','02215','02364','01805','01523','02420','02421','01773','01773','01460','01901','01902','01903','01904','01905','01910','01940','01930','02148','01944','01944','02345','02031','02048','01945','02171','01752','01752','02020','02041','02047','02050','02051','02059','02065','02051','02051','02204','01889','02204','02126','01754','02052','02153','02155','02156','02053','01813','02176','01756','01945','01949','01757','01504','02054','01529','02186','02187','02055','02120','01908','02045','01760','01807','02492','02494','02494','02494','02492','02456','01922','01951','01950','01951','02456','02458','02459','02460','02461','02462','02464','02465','02466','02467','02468','02495','02459','02459','02459','02461','02461','02462','02462','02464','02464','02458','02460','02462','01760','02171','02495','02056','02171','02762','02140','02355','02764','01523','02059','01760','02358','02171','01864','01889','02060','01776','02451','02452','02455','02191','02712','02766','02018','02061','02062','02065','02558','01960','01961','02358','02359','01966','01460','02762','01950','01951','02345','02360','02361','02362','02381','02140','01965','01965','02169','02170','02171','02269','02169','02368','01867','02136','02137','02151','02151','02458','02370','01966','02364','02131','01969','02118','02119','02120','02120','01970','01971','01952','01952','01952','01906','01701','02040','02055','02060','02066','02066','02066','03874','02044','02067','02070','01770','01464','01464','02493','02364','01561','01760','02163','02143','02144','02145','02127','02366','01982','01561','01940','01760','02169','02071','02453','02190','01745','01772','01745','01772','02171','02206','01467','02180','02493','02072','01775','01776','01907','02718','02780','02783','01983','01469','01474','02153','02125','01568','01718','01718','01718','02468','01880','02032','02071','02081','02451','02452','02453','02454','02455','02571','02471','02472','02477','02471','02479','01778','02340','02457','02481','02482','02481','02481','02481','01984','01720','01742','02339','01905','02155','02156','02465','01960','02169','02132','02144','01474','01568','02576','02493','02090','02188','02189','02190','02191','02188','02190','02381','02381','01887','01890','02145','02152','01801','01807','01813','01815','01888','02170','01784','02070','02093']

#***************  referenced Org bundles ******

def get_bundle(in_path, in_file):  # as python model
    with open(f'{in_path}/{in_file}.json') as f:
        logging.info(f'reading file = {in_file}')
        return B.Bundle(load(f))

#orgs = get_bundle(out_path, org_file)
#parent_orgs = get_bundle(out_path, managing_org_file)
#pract_roles = get_bundle(out_path, pract_org_file)
#{x: x**2 for x in (2, 4, 6)}
bundles = {k:get_bundle(out_path,v) for k,v in example_files.items()}

#***************  Functions *********************

def get_zip(postal_code):  # get 5 digit code include the leading 0
  if len(postal_code) <= 5:
    return(postal_code)
  else:
    return(postal_code[:-4])


def get_f_id(f_type,npi,source=None):
    if source:
        f_type = f'{source}-{f_type}'
    return f'vhdir-{f_type}-{npi}'


def get_csv(in_path,in_file):
    with open(f'{in_path}/{in_file}.csv') as f:
        logging.info(f'reading file = {in_file}')
        my_list = [j for j in csv.DictReader(f, restkey='foo_id', restval=None, dialect='excel')]
    return my_list


def get_bundle(in_path, in_file):  # as py fhir bundle class
    with open(f'{in_path}/{in_file}.json') as f:
        logging.info(f'reading file = {in_file}')
        return B.Bundle(load(f))

def scrub_dict(d):
    unwanted = ['', u'', None, [], {}, 'None', -1]
    if type(d) is dict:
        return dict((k, scrub_dict(v)) for k, v in d.items() if v not in unwanted and scrub_dict(v))
    elif type(d) is list:
        return [scrub_dict(v) for v in d if v not in unwanted and scrub_dict(v)]
    else:
        return d


def get_xml(server, body, type):

    x_params ={
        '_count':500
        }

    r = put(url=f'{server}/Bundle/vhdir-{type}-examples-bundle', data=body.encode('utf-8'), headers=j_headers)
    logging.info(f'put json status_code = {r.status_code}')
    logging.info(f'body as json = \n{dumps(r.json(), indent =3)}')

    r = get(url=f'{server}/Bundle/vhdir-{type}-examples-bundle', headers=x_headers, params=x_params)
    logging.info(f'get xml status_code = {r.status_code}')
    return r.content  # may not work if large


def write_bundle(out_path,f_type,file,source=None, format='json'):

    if source == f_type:
        r_type = source
    else:
        r_type = f'{source}-{f_type}'

    for out_folder in out_folders:
        try:
            os.mkdir(f'{out_path}/{out_folder}{f_type}')
        except FileExistsError:
            pass

        with open(f'{out_path}/{out_folder}{f_type}/vhdr-{r_type}-example-bundle.{format}', 'w' if format == 'json' else 'wb') as f:
            logging.info(f'writing to file = {out_path}/{out_folder}{f_type}/vhdr-{r_type}-example-bundle.{format}')
            f.write(file)


def write_resource_csv(f_type,data):
    for out_folder in out_folders:
        with open(f'{out_path}/{out_folder}{f_type}/sample-nppes-{f_type}-data.csv', mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, dialect='excel', quoting=csv.QUOTE_ALL)
            writer.writerow(['NPI','Resource ID','Name','References List'])
            for line in data:
                writer.writerow(line)

def post_bundle(server,body): #upload to fhir server

    r = post(url=f'{server}', data=body.encode('utf-8'), headers=j_headers)
    logging.info(f'status code for posting batch bundle: {r.status_code}')



#****************  Main  *************************

def main(f_type,id_list,source):

    f_Type=rr.r_map[source]

    entries = []

    if f_type == 'managing-org':
        for item in get_csv(in_path,'managing_orgs_data'): #  get sample data from csv
            npi = item['id']
            f_id=get_f_id(f_type,npi)
            logging.info(f'create resource id = {f_id}')
            example = f_templ.managing_org(item,f_id,f_type,npi)  # create dict using fstring template
            example = scrub_dict(example)  # scrub out nulls
            id_list[snakecase(f_type)].append((npi,f'{f_Type}/{f_id}',item['name']))
            entries.append(f_templ.entries_templ(server_path,example,f_Type,f_id))  # create dict using fstring template

    elif f_type == 'coverage':
        for state in states:
            f_id=get_f_id(f_type,spinalcase(state.lower()),source)

            attachment = {
              'contentType' : 'application/vnd.geo+json',  # Mime type of the content, with charset etc.
              'data' : b64.geojson_b64[snakecase(state.lower())].decode('ascii'),  # Data inline, base64ed
              'title' : f'GeoJSON for {state}',  # Label to display in place of the data
              'creation' : timestamp  # Date attachment was first created
            }

            logging.info(f'create resource id = {f_id}')
            example = f_templ.coverage(name=state, attachment=attachment)  # create dict using fstring template
            id_list[snakecase(f_type)].append((state,f'{f_Type}/{f_id}',state))
            entries.append(f_templ.entries_templ(server_path,example,f_Type,f_id))  # create dict using fstring template

    elif f_type == 'insuranceplan':
        for item in get_csv(in_path,'managing_orgs_data'): #  get sample data from csv
            npi = item['plan_id']
            f_id=get_f_id(f_type,npi)
            if item['is_plan'] == "TRUE":
                logging.info(f'create resource id = {f_id}')
                example = f_templ.insuranceplan(item)  # create dict using fstring template
                example = scrub_dict(example)  # scrub out nulls
                id_list[snakecase(f_type)].append((item['plan_id'],f'{f_Type}/{f_id}',item['plan_name']))
                entries.append(f_templ.entries_templ(server_path,example,f_Type,f_id))  # create dict using fstring template


    elif f_type == 'hie-orgaffiliation':
        for entry in bundles['orgs'].entry:
            z = get_zip(entry.resource.address[0].postalCode)
            st = entry.resource.address[0].state
            hie_list=[]
            if z in western_ma_zips:
                hie_list.append(('wma','Western Massachusetts HIE'))

            if st == 'RI':
                hie_list.append(('ri','Rhode Island HIE'))

            if z in hartford_zips:
                hie_list.append(('hct','Hartford Connecticut HIE'))

            for hie_item in hie_list:
                prefix = f'hie-{hie_item[0]}'
                parent_org = next(po for po in bundles['managing_orgs'].entry if po.resource.name == hie_item[1])  # get parent org
                logging.info(f'{hie_item[1]} orgaffiliation for org resource id = {entry.resource.id}')
                example = f_templ.hie_orgaffiliation(org=entry.resource, parent_org=parent_org.resource, prefix=prefix)  # create dict using fstring template
                oa = OA.OrganizationAffiliation(example) # instantiate as orgaffiliation
                id_list[snakecase(f_type)].append((oa.identifier[0].value,f'{f_Type}/{oa.id}',oa.organization.display))
                entries.append(f_templ.entries_templ(server_path,example,f_Type,{oa.id}))  # create dict using fstring template

    elif f_type == 'addin-org-role':


        for n_entry in bundles['networks'].entry:
            network = n_entry.resource
            if network.name in addin_networks.keys():
                for o_entry in bundles['orgs'].entry:
                    org = o_entry.resource
                    z = get_zip(org.address[0].postalCode)
                    if (org.address[0].state == addin_networks[network.name][1] or
                    (addin_networks[network.name][1] == "Greater Hartford Area" and z in hartford_zips)):
                        # add org-affil to orgaffil bundle
                        logging.info(f'orgaffiliation for org resource id = {network.name}')
                        example = f_templ.hie_orgaffiliation(org=org, parent_org=network, prefix=addin_networks[network.name][0])  # create dict using fstring template
                        oa = OA.OrganizationAffiliation(example) # instantiate as orgaffiliation
                        be = B.BundleEntry(f_templ.entries_templ(server_path,example,f_Type,{oa.id}))

                        bundles['org_roles'].entry.append(be)  # create lsit of classes to append to existing bundle
        for oa_entry in bundles['org_roles'].entry:
            logging.info(oa_entry.resource.id)
            logging.info(oa_entry.resource.organization.display)
            id_list[snakecase(f_type)].append((oa_entry.resource.id,f'{f_Type}/{oa_entry.resource.id}',oa_entry.resource.organization.display))


    elif f_type == 'addin-pract-role':
        p_bundles = [v for k,v in bundles.items() if k in ['pract0','pract1','pract2','pract3']]
        for n_entry in bundles['networks'].entry:
            network = n_entry.resource
            if network.name in addin_networks.keys():
                for p_bundle in p_bundles:
                    for p_entry in p_bundle.entry:
                        pract = p_entry.resource
                        z = get_zip(pract.address[0].postalCode)
                        if (pract.address[0].state == addin_networks[network.name][1] or
                        (addin_networks[network.name][1] == "Greater Hartford Area" and z in hartford_zips)):
                            # add pract-affil to practrole bundle
                            logging.info(f'practitionerrole for pract = {pract.name[0].text}')
                            example = f_templ.network_member_practrole(member=pract, network=network, prefix=addin_networks[network.name][0])  # create dict using fstring template
                            pr = PR.PractitionerRole(example) # instantiate as practitionerrole
                            be = B.BundleEntry(f_templ.entries_templ(server_path,example,f_Type,{pr.id}))
                            bundles['pract_roles'].entry.append(be)  # create lsit of classes to append to existing bundle
        for pr_entry in bundles['pract_roles'].entry:
            logging.info(pr_entry.resource.id)
            logging.info(pr_entry.resource.organization.display)
            id_list[snakecase(f_type)].append((pr_entry.resource.id,f'{f_Type}/{pr_entry.resource.id}',pr_entry.resource.organization.display))


    elif f_type == 'endpoint':
        for k,v in bundles.items():
            logging.info(f'for {k} create endpoints...')
            for entry in v.entry:
                try:
                    example = f_templ.endpoint(r=entry.resource)  # create dict using fstring template
                    #logging.info(f'example = \n{example}')
                    ep = EP.Endpoint(example) # instantiate as endpoint
                    id_list[snakecase(f_type)].append((ep.id,f'{f_Type}/{ep.id}',ep.name))
                    entries.append(f_templ.entries_templ(server_path,example,f_Type,{ep.id}))  # create dict using fstring template
                except AttributeError:
                    pass




    logging.info(f'type = {f_type}')
    if f_type not in addins.keys():
        batch_bundle = f_templ.batch_bundle_template(f_type,entries) # create dict using fstring template
        batch_json = dumps(batch_bundle, indent=3, ensure_ascii=False)
        logging.info(f'{f_type} batch_bundle as json') # as dict
        fhir_file = B.Bundle(batch_bundle)  # validate file
        #logging.info(f'bundle looks like = {json_file}')
        write_bundle(out_path,f_type,batch_json,source,'json')  # save to file

        write_resource_csv(spinalcase(f_type),resource_keys[snakecase(f_type)])

        # TODO convert to xml
        xml_bundle = get_xml(convert_server,batch_json,f_type)#use fhir server to convert bundle xml to json
        write_bundle(out_path,f_type,xml_bundle,source,'xml')  #save to file
        post_bundle(server_path,batch_json) #upload to fhir server

    else:  # append to existing bundle
        batch_json = dumps(bundles[addins[f_type][1]].as_json(), indent=3, ensure_ascii=False)  # convert to json byte
        write_bundle(out_path,addins[f_type][0],batch_json,addins[f_type][0],'json') # save to file

        # TODO convert to xml

        xml_bundle = get_xml(convert_server,batch_json,addins[f_type][0])#use fhir server to convert bundle xml to json
        write_bundle(out_path,addins[f_type][0],xml_bundle,addins[f_type][0],'xml')  #save to file

        post_bundle(server_path,batch_json) #upload to fhir server

        write_resource_csv(spinalcase(addins[f_type][0]),resource_keys[snakecase(f_type)])

    return

#********************* __name__ == "__main__" ********************

#This only happens when this module is called directly:
if __name__ == "__main__":
    resource_keys = dict(  # create a map of resource_ids to create a relational table
        managing_org=[],
        hie_orgaffiliation=[],
        endpoint=[],
        coverage=[],
        insuranceplan=[],
        addin_org_role=[],
        addin_pract_role=[]
        )

#*********** REMEMBER is spinalcase below as apposed to snakecase above *****

    #main('managing-org',resource_keys,'organization')
    #main('hie-orgaffiliation',resource_keys,'organizationaffiliation')
    main('endpoint',resource_keys,'endpoint')
    #main('coverage',resource_keys,'location')
    #main('insuranceplan',resource_keys,'insuranceplan')
    #main('addin-org-role',resource_keys,'organizationaffiliation')
    #main('addin-pract-role',resource_keys,'practitionerrole')





    logging.debug('end of program')
