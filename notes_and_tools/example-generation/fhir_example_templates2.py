from datetime import datetime
import lat_long_byzip as ll
from stringcase import spinalcase, titlecase, snakecase
from string import punctuation
from operator import attrgetter

import os, sys, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')


timestamp = f'{datetime.utcnow().isoformat()}Z'

def get_zip(postal_code):  # get 5 digit code
  if len(postal_code) <= 5:
    return(postal_code.lstrip('0'))
  else:
    return(postal_code[:-4].lstrip('0'))

def urlify(s):
    for c in punctuation:
        s= s.replace(c,'')
    s = s.lower()
    s = spinalcase(s)
    return f'https://{s}.com'

def slugify(s):
    for c in punctuation:
        s= s.replace(c,'')
    s = s.lower()
    s = spinalcase(s)
    return s

def safecall(funct,exception,default):
    try:
        return funct.as_json()
    except exception:
        return default


def get_partof(id, display):
    if id:
        return {
    'reference': f'Organization/vhdir-managing-org-{id}',
    'display': display
     }
    else:
        return None


#***********************bundle_templates******************************

def batch_bundle_template(f_type,entries):

    return {
        'resourceType' : 'Bundle',
        'id': f'vhdir-{f_type}-examples-bundle',
        'type' : 'batch',
        'timestamp' : timestamp,
        'entry' : entries
        }


def entries_templ(server_path,example,f_Type,f_id):
    return {
        'fullUrl' : f'{server_path}/{f_Type}/{f_id}',
        'resource' : example,
         'request' : {
          'method' : 'PUT',
          'url' : f'{f_Type}/{f_id}'
         }
        }


#***********************managing_org_template******************************


def managing_org(item,f_id,f_type,npi):

    type_display = dict(
    prov = 'HealthCare Provider',
    ins = "Insurance Company",
    pay = "Payer"
    )



    return {
        'resourceType': 'Organization',
        'id': f_id,
        'meta': {
            'profile': [
                'http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-organization'
            ]
        },
        'identifier': [
            {
                'extension': [
                    {
                        'url': 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/identifier-status',
                        'valueCode': 'active'
                    }
                ],
                'use': 'official',
                'type': {
                    'coding': [
                        {
                            'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                            'code': 'NPI',
                            'display': 'National provider identifier'
                        }
                    ],
                    'text': 'NPI'
                },
                'system': 'http://hl7.org/fhir/sid/us-npi',
                'value': npi,
                'period': {
                    'start': '2004-04-21T11:57:00-05:00'
                },
                'assigner': {
                    'display': 'Centers for Medicare and Medicaid Services'
                }
            }
        ],
        'active': True,
        'type': [
            {
                'coding': [
                    {
                        'system': 'http://terminology.hl7.org/CodeSystem/organization-type',
                        'code': item["type"],
                        'display': type_display[item["type"]]
                    }
                ],
                'text':  type_display[item["type"]]
            }
        ],
        'name': item["name"],
        'telecom': [
            {
                'system': 'phone',
                'value': item["phone"] if item["phone"] else "5555555555"
            }
        ],
        'address': [
            {
                'extension': [
                    {
                        'extension': [
                            {
                                'url': 'latitude',
                                'valueDecimal': ll.lat_long[get_zip(item["zip"])][0]
                            },
                            {
                                'url': 'longitude',
                                'valueDecimal': ll.lat_long[get_zip(item["zip"])][1]
                            }
                        ],
                        'url': 'http://hl7.org/fhir/StructureDefinition/geolocation'
                    }
                ],
                'use': 'work',
                'type': 'both',
                'text': f'{item["address"]}, {item["city"]}, {item["state"]} {item["zip"]}',
                'line': [
                    item["address"]
                ],
                'city': item["city"],
                'state': item["state"],
                'postalCode': item["zip"],
                'country': 'USA'
            }

        ],
        'partOf': get_partof(item["partof_id"], item["partof_display"]),
        'contact': [
            {
                'purpose': {
                    'coding': [
                        {
                            'system': 'http://terminology.hl7.org/CodeSystem/contactentity-type',
                            'code': 'ADMIN',
                            'display': 'Administrative'
                        }
                    ]
                },
                'name': {
                    'use': 'official',
                    'text': 'Kathy Contact',
                    'family': 'Contact',
                    'given': [
                        'Kathy'
                    ]
                },
                'telecom': [
                    {
                        'extension': [
                            {
                                'extension': [
                                    {
                                        'url': 'daysOfWeek',
                                        'valueCode': 'mon'
                                    },
                                    {
                                        'url': 'daysOfWeek',
                                        'valueCode': 'tue'
                                    },
                                    {
                                        'url': 'daysOfWeek',
                                        'valueCode': 'wed'
                                    },
                                    {
                                        'url': 'daysOfWeek',
                                        'valueCode': 'thu'
                                    },
                                    {
                                        'url': 'daysOfWeek',
                                        'valueCode': 'fri'
                                    },
                                    {
                                        'url': 'availableStartTime',
                                        'valueTime': '07:00:00'
                                    },
                                    {
                                        'url': 'availableEndTime',
                                        'valueTime': '18:00:00'
                                    }
                                ],
                                'url': 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/contactpoint-availabletime'
                            }
                        ],
                        'system': 'phone',
                        'value': item["phone"],
                        'use': 'work'
                    }
                ]
            }
        ],
        'endpoint': [
            {
                'reference': f'Endpoint/{f_id}-direct',
                'display': f'{item["name"]} Direct address'
            }
        ]
    }

#***********************hie org affiliation template******************************

def hie_orgaffiliation(org, parent_org, prefix):
  return {
    'resourceType' : 'OrganizationAffiliation',
    'id': f'vhdir-{prefix}-organizationrole-{org.identifier[0].value}',
    'meta': {
        'profile': [
            'http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-organizationaffiliation'
        ]
    },
    'identifier' : [
      {
        'extension' : [
          {
            'url' : 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/identifier-status',
            'valueCode' : 'active'
          }
        ],
        'use' : 'secondary',
        'type' : {
          'text' : 'member hospital'
        },
        'system' : f'http://example.org/www.{urlify(parent_org.name)}',
        'value' : f'{slugify(org.name)}-999',
        'assigner' : {
          'reference' : f'Organization/{parent_org.id}',
          'display' : parent_org.name
        }
      }
    ],
    'active' : True,
    'organization' : {
          'reference' : f'Organization/{parent_org.id}',
          'display' : parent_org.name
    },
    'participatingOrganization' : {
      'reference' : f'Organization/{org.id}',
      'display' : org.name
    },
    'code' : [
      {
        'coding' : [
          {
            'system' : 'http://hl7.org/fhir/organization-role',
            'code' : 'member',
            'display' : 'Member'
          }
        ],
        'text' : 'Hospital member'
      }
    ],
        'endpoint': [
            {
                'reference': f'Endpoint/vhdir-hie-organizationaffiliation-{org.identifier[0].value}-direct',
                'display': f'Direct address for {org.name} {parent_org.name} Member Role'
            }
        ]
  }

#************************** endpoint template ********************************


def endpoint(r): # r = resource as python class

    ep_map = dict(
    PractitionerRole=('organization','practitioner.display','organization.display'),
    Organization=(None,'name','name'),
    OrganizationAffiliation=('organization','organization.display','organization.display'),
    Location=('managingOrganization','name','managingOrganization.display'),
    HealthcareService=('providedBy','name','providedBy.display'),
    InsurancePlan=('ownedBy','name','ownedBy.display')
    )

    try:
        mo=getattr(r,ep_map[r.resource_type][0])
    except TypeError:
        mo = None
    except KeyError:  # no endpoint
        return

    address1=attrgetter(ep_map[r.resource_type][1])(r)
    address2=attrgetter(ep_map[r.resource_type][2])(r)


    return {
      'resourceType' : 'Endpoint',
      'id' : r.endpoint[0].reference[9:],
      'meta' : {
        'profile' : [
          'http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-endpoint'
        ]
      },
#      'extension' : [
#        {
#          'url' : 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/endpoint-usecase',
#          'extension' : [
#            {
#              'url' : 'type',
#              'valueCodeableConcept' : {
#                'coding' : [
#                  {
#                    'system' : 'http://hl7.org/fhir/uv/vhdir/CodeSystem/usecase',
#                    'code' : 'treatment',
#                    'display' : 'treatment'
#                  }
#                ]
#              }
#            },
#            {
#              'url' : 'standard',
#              'valueUri' : 'http://wiki.directproject.org/file/view/2011-03-09%20PDF%20-%20XDR%20and%20XDM%20for%20Direct%20Messaging%20Specification_FINAL.pdf'
#            }
#          ]
#        },
#        {
#          'url' : 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/endpoint-rank',
#          'valuePositiveInt' : 1
#        },
#        {
#          'url' : 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/digitalcertificate',
#          'extension' : [
#            {
#              'url' : 'type',
#              'valueCoding' : {
#                'system' : 'http://hl7.org/fhir/uv/vhdir/CodeSystem/digitalcertificate',
#                'code' : 'grp',
#                'display' : 'Group'
#              }
#            },
#            {
#              'url' : 'use',
#              'valueCoding' : {
#                'system' : 'http://hl7.org/fhir/uv/vhdir/CodeSystem/digitalcertificate',
#                'code' : 'signing',
#                'display' : 'Signing'
#              }
#            },
#            {
#              'url' : 'use',
#              'valueCoding' : {
#                'system' : 'http://hl7.org/fhir/uv/vhdir/CodeSystem/digitalcertificate',
#                'code' : 'encrypt',
#                'display' : 'Encryption'
#              }
#            },
#            {
#              'url' : 'certificateStandard',
#              'valueCoding' : {
#                'system' : 'http://hl7.org/fhir/uv/vhdir/CodeSystem/digitalcertificate',
#                'code' : 'x.509v3',
#                'display' : 'x.509v3'
#              }
#            },
#            {
#              'url' : 'certificate',
#              'valueString' : 'VGhpcyBpcyB0aGUgZGlnaXRhbCBjZXJ0aWZpY2F0ZSBhc3NvY2lhdGVkIHdpdGggdGhlIEZvdW5kaW5nIEZhdGhlcnMgSGVhcnQgYW5kIFZhc2N1bGFyIEluc3RpdHV0ZeKAmXMgRGlyZWN0IGFkZHJlc3MNCg0KLS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0NCk1JR2ZNQTBHQ1NxR1NJYjNEUUVCQVFVQUE0R05BRENCaVFLQmdRQysrM3RvczN4cTVhSWFKLzZSREd6REZKK2YNCjJNWkxHdHEyZXM5T1NRdEpzYU9YNjd6VlI5QnpMZWgwa2pMZ3ZOMC85Q0NxNDdQS3dvQWV4b2R2MXVhanF3YWcNCnBHYlV0NkF5ZHEzeE9LMllhRnkzTDVMMXBHc2NySzJPMXJSd0ExYUpndXdRVjArM0xYNmVwOExBVitkZFVaS3cNCjB4MlRyUkRZUUJFZE52YkFVd0lEQVFBQg0KLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0tDQo='
#            },
#            {
#              'url' : 'expirationDate',
#              'valueDate' : '2019-04-07'
#            },
#            {
#              'url' : 'trustFramework',
#              'valueCodeableConcept' : {
#                'coding' : [
#                  {
#                    'system' : 'http://hl7.org/fhir/uv/vhdir/CodeSystem/digitalcertificate',
#                    'code' : 'direct',
#                    'display' : 'DirectTrust'
#                  }
#                ]
#              }
#            }
#          ]
#        }
#      ],
      'status' : 'active',
      'connectionType' : {
        'system' : 'http://terminology.hl7.org/CodeSystem/endpoint-connection-type',
        'code' : 'direct-project',
        'display' : 'Direct Project'
      },
      'name' : r.endpoint[0].display,
      'managingOrganization' : {
        'reference' : mo.reference if mo else f'Organization/{r.id}',
        'display' : mo.display if mo else r.name
      },
      'contact' : [r.telecom[0].as_json() if r.telecom else {'value' : '5555555555'}],
      'period' : {
        'start' : '2018-11-19'
      },
      'payloadType' : [
        {
          'coding' : [
            {
              'system' : 'urn:oid:1.3.6.1.4.1.19376.1.2.3',
              'code' : 'urn:ihe:pcc:xphr:2007',
              'display' : 'HL7 CCD Document'
            }
          ]
        }
      ],
      'payloadMimeType' : [
        'application/hl7-v3+xml'
      ],
      'address' : f'mailto:{slugify(address1)}'
                  f'@direct.{slugify(address2)}.org'
    }


# ********* Location for Coverage Location ********************

def coverage(name, attachment):
    return {
      'resourceType' : 'Location',
      'id' : f'vhdir-coverage-location-{slugify(name)}',
      'meta' : {
        'profile' : [
          'http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-location'
        ]
      },
      'extension' : [

    {
        "url" : "http:#hl7.org/fhir/StructureDefinition/location-boundary-geojson",  # R!
        "valueAttachment" : attachment  # Value of extension
      }
      ],
      'identifier' : [
        {
          'extension' : [
            {
              'url' : 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/identifier-status',
              'valueCode' : 'active'
            }
          ],
          'use' : 'secondary',
          'system' : 'http://example.org/vhdir.com',
          'value' : slugify(name)
          }
      ],
      'status' : 'active',
      'name' : name,
      'description' : f'Coverage Area for {name}',
    #   'type' : [
    #     {
    #       'coding' : [
    #         {
    #           'system' : 'http://terminology.hl7.org/CodeSystem/v3-RoleCode',
    #           'code' : 'HOSP',
    #           'display' : 'Hospital',
    #           'userSelected' : True
    #         }
    #       ]
    #     }
    #   ],
      'physicalType' : {
        'coding' : [
          {
            'system' : 'http://terminology.hl7.org/CodeSystem/location-physical-type',
            'code' : 'jdn',
            'display' : 'Jurisdiction',
          }
        ]
      },
    }

#******************  InsurancePlan template ************************


def insuranceplan(item):

    plan_map = dict(
    cat='Catastrophic', # 'Catastrophic' health insurance plans have low monthly premiums and very high deductibles. They may cover worst-case scenarios, like getting seriously sick or injured. Patient pays most routine medical expenses.
    bronze='Bronze',  # 'Bronze' type plan defines the estimated split costs of the plan, where patient is responsible for 40% of their healthcare cost while 60% is covered by the plan.
    bronzeexp='Expanded Bronze',  # The 'extended bronze' plan is an addition to the bronze metal level which establishes the de minimis variation range for the actuarial value (AV) level of coverage to allow variation in the AV to -4/+2 percentage points.
    silver='Silver',  # 'Silver' type plan defines the estimated split costs of the plan, where patient is responsible for 30% of their healthcare cost while 70% is covered by the plan.
    gold='Gold',  # 'Gold' type plan defines the estimated split costs of the plan, where patient is responsible for 20% of their healthcare cost while 80% is covered by the plan.
    platinum='Platinum', # 'Platinum' type plan defines the estimated split costs of the plan, where patient is responsible for 10% of their healthcare cost while 90% is covered by the plan.
    lowded='Low deductible', # A health insurance plan with higher premiums and lower out of pocket cost than a traditional health plan.
    highded ='High deductible'
    )

    return {
      'resourceType' : 'InsurancePlan',
      'id': f'vhdir-insuranceplan-{item["plan_id"]}',
      'identifier' : [
        {
          'use' : 'official',
          'type' : {
            'text' : 'HIOS product ID'
          },
          'system' : 'https://www.cms.gov/CCIIO/',
          'value' : item["plan_id"],
          'assigner' : {
            'display' : 'Centers for Medicare and Medicaid Services'
          }
        }
      ],
      'status' : 'active',
      'type' : [  # how is this different than coverage.type?
        {
         'text' : plan_map[item['plan_type']],
          'coding' : [
            {
              'system' : 'http://hl7.org/fhir/uv/vhdir/CodeSystem/payercharacteristics',
              'code' : item['plan_type'],
              'display' : plan_map[item['plan_type']]
            }
          ]
        }
      ],
      'name' : item['plan_name'],
      'alias' : [
        item['plan_alias']
      ],
      'period' : {
        'start' : '2019-01-01',
        'end' : '2020-01-01'
      },
      'ownedBy' : {
        'reference' : f'Organization/vhdir-managing-org-{item["id"]}',
        'display' : item['name']
      },
      'administeredBy' : {
        'reference' : f'Organization/vhdir-managing-org-{item["plan_manager_id"]}',
        'display' : item['plan_manager']
      },
      'coverageArea' : [
        {
          'reference' : f'vhdir-location-coverage-{slugify(item["coverage"])}',
          'display' : item['coverage']
        }
      ],
      'contact' : [
        {
          'purpose' : {
            'coding' : [
              {
                'system' : 'http://terminology.hl7.org/CodeSystem/contactentity-type',
                'code' : 'PATINF',
                'display' : 'Patient'
              }
            ],
            'text' : 'General information'
          },
          'telecom' : [
            {
              'system' : 'phone',
              'value' : item["phone"]
            },
            {
              'system' : 'email',
              'value' : item["url"]
            }
          ]
        }
      ],
        'endpoint': [
            {
                'reference': f'Endpoint/item["plan_id"]-direct',
                'display': f'{item["plan_name"]} Direct address'
            }
        ],
      'network' : [
        {
          'reference' : f'Organization/vhdir-organization-{item["network_id"]}',
          'display' : item['network_name']
        }
      ],
      'coverage' : [  # just one coverage for now
        {
          'type' : {
            'coding' : [
              {
                'code' : 'medical',
                'display' : 'Medical'
              }
            ],
            'text' : 'Coverage related to medical inpatient, outpatient, diagnostic, and preventive care'
          },
          'network' : [
            {
              'reference' : f'Organization/vhdir-organization-{item["network_id"]}',
              'display' : item['network_name']
            }
          ],
          'benefit' : [  # just default to these for now
          {
              'type' : {
                'text' : 'Routine Wellness Exam (Adult) – Adult'
              },
              'requirement' : 'N/A',
                'limit' : [
                {
                  'value' : {
                    'value' : 1,
                    'unit' : 'visit/yr',
                    'system' : 'http://unitsofmeasure.org',
                    'code' : '{visit}/a'
                  },
                  'code' : {
                   'text' : 'annually'  # this value set even as an example is innappropriate
                  }
                 }
               ]
            },
            {
              'type' : {
                'coding' : [
                  {
                    'code' : '001',
                    'display' : 'Primary care visit to treat an injury or illness'
                  }
                ]
              },
              'requirement' : 'N/A',
              'limit' : [
                {
                  'code' : {
                    'text' : 'unlimited'
                  }
                }
              ]
            }
          ]
        }
#        {
#          'type' : {
#            'coding' : [
#              {
#                'code' : 'dental',
#                'display' : 'Dental'
#              }
#            ],
#            'text' : 'Coverage related to dental care'
#          },
#          'network' : [
#            {
#              'reference' : 'Organization/patriotdental',
#              'display' : 'Patriot Dental Provider Network'
#            }
#          ],
#          'benefit' : [
#            {
#              'type' : {
#                'coding' : [
#                  {
#                    'code' : '052',
#                    'display' : 'Basic Dental Care – Adult'
#                  }
#                ],
#                'text' : 'Periodic oral checkup'
#              },
#              'requirement' : 'N/A',
#                {
#                  'value' : {
#                    'value' : 2,
#                    'unit' : 'visit/yr',
#                    'system' : 'http://unitsofmeasure.org',
#                    'code' : '{visit}/a'
#                  },
#                  'code' : {
#                    'text' : 'biannual oral checkup'
#                  }
#                }
#              ]
#            }
#          ]
#        }
      ]
    }  # for now omit IP.plan element until use case fleshed out where is needed.


#************************* provider-member practitioner role template **********

def network_member_practrole(member, network, prefix):

    return {
          'resourceType' : 'PractitionerRole',
          'id': f'vhdir-{prefix}-practitionerrole-{member.identifier[0].value}',
          'meta' : {
            'profile' : ['http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-practitionerrole']
          },
          'identifier' : [{
            'extension' : [{
              'url' : 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/identifier-status',
              'valueCode' : 'active'
            }],
            'use' : 'secondary',
            'type' : {
              'coding' : [{
                'system' : 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'code' : 'PRN',
                'display' : 'Provider number'
              }],
              'text' : 'Network Provider ID'
            },
            'system' : f'http://example.org/www.{urlify(network.name)}',
            'value' : f'{member.name[0].given[0][0].lower()}{member.name[0].family.lower()}{member.birthDate.as_json().replace("-","")}',
            'period' : {
              'start' : '2019-01-01'
            }
          }],
          'active' : True,
          'period' : {
            'start' : '2019-01-01'
          },
          'practitioner' : {
            'reference' : f'Practitioner/{member.id}',
            'display' : f'{member.name[0].text}, {member.name[0].suffix[0] if member.name[0].suffix else None}'
          },
          'organization' : {
            'reference' : f'Organization/{network.id}',
            'display' : network.name
          },
          'code' : [{
            'text' : 'Provider Member'
          }],
          'telecom' : [{
            'system' : 'phone',
            'value' : member.telecom[0].value if member.telecom[0].value else '5555555555'
          }],
          'endpoint' : [{
            'reference': f'vhdir-{prefix}-practrole-{member.identifier[0].value}-direct',
            'display': f'Direct address for {member.name[0].text} {network.name} Member Role'
        }]
        }
