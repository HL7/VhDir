from json import dumps, loads, load
from fhirr4models import bundle as B
from fhirr4models import practitioner as P
from fhirr4models import organization as O
from fhirr4models import organizationaffiliation as OA
from fhirr4models import practitionerrole as PR
from fhirr4models import endpoint as EP
from string import punctuation
from stringcase import spinalcase, titlecase, snakecase
from pprint import pprint
from operator import attrgetter
def slugify(s):
    for c in punctuation:
        s= s.replace(c,'')
    s = s.lower()
    s = spinalcase(s)
    return s

r_dict =  {
                'resourceType': 'PractitionerRole',
                'id': 'vhdir-practitionerrole-9997556504-1',
                'meta': {
                    'profile': [
                        'http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-practitionerrole'
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
                        'use': 'secondary',
                        'type': {
                            'coding': [
                                {
                                    'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                                    'code': 'PRN',
                                    'display': 'Provider number'
                                }
                            ],
                            'text': 'Network Provider ID'
                        },
                        'system': 'https://persona.com',
                        'value': '9845259',
                        'period': {
                            'start': '2016-02-22'
                        },
                        'assigner': {
                            'display': 'Persona of Connecticut'
                        }
                    }
                ],
                'active': True,
                'period': {
                    'start': '2016-02-22'
                },
                'practitioner': {
                    'reference': 'Practitioner/vhdir-practitioner-9997556504',
                    'display': 'María Elena Chacón'
                },
                'organization': {
                    'reference': 'Organization/vhdir-organization-HPID060000',
                    'display': 'CT Silver 70 PPO'
                },
                'code': [
                    {
                        'text': 'Provider Member'
                    }
                ],
                'telecom': [
                    {
                        'system': 'phone',
                        'value': '2039259600'
                    }
                ],
                'endpoint': [
                    {
                        'reference': 'Endpoint/vhdir-practitionerrole-9997556504-1-direct',
                        'display': 'Direct address for María Elena Chacón Network Member Role'
                    }
                ]
            }




def endpoint(r): # r = resource as python class
    return {
      'resourceType' : 'Endpoint',
      'id' : r.endpoint[0].reference[9:],
      'meta' : {
        'profile' : [
          'http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-endpoint'
        ]
      },
      'extension' : [
        {
          'url' : 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/endpoint-usecase',
          'extension' : [
            {
              'url' : 'type',
              'valueCodeableConcept' : {
                'coding' : [
                  {
                    'system' : 'http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-usecase',
                    'code' : 'treatment',
                    'display' : 'treatment'
                  }
                ]
              }
            },
            {
              'url' : 'standard',
              'valueUri' : 'http://wiki.directproject.org/file/view/2011-03-09%20PDF%20-%20XDR%20and%20XDM%20for%20Direct%20Messaging%20Specification_FINAL.pdf'
            }
          ]
        },
        {
          'url' : 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/endpoint-rank',
          'valuePositiveInt' : 1
        },
        {
          'url' : 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/digitalcertificate',
          'extension' : [
            {
              'url' : 'type',
              'valueCoding' : {
                'system' : 'http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-digitalcertificate',
                'code' : 'grp',
                'display' : 'Group'
              }
            },
            {
              'url' : 'use',
              'valueCoding' : {
                'system' : 'http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-digitalcertificate',
                'code' : 'signing',
                'display' : 'Signing'
              }
            },
            {
              'url' : 'use',
              'valueCoding' : {
                'system' : 'http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-digitalcertificate',
                'code' : 'encrypt',
                'display' : 'Encryption'
              }
            },
            {
              'url' : 'certificateStandard',
              'valueCoding' : {
                'system' : 'http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-digitalcertificate',
                'code' : 'x.509v3',
                'display' : 'x.509v3'
              }
            },
            {
              'url' : 'certificate',
              'valueString' : 'VGhpcyBpcyB0aGUgZGlnaXRhbCBjZXJ0aWZpY2F0ZSBhc3NvY2lhdGVkIHdpdGggdGhlIEZvdW5kaW5nIEZhdGhlcnMgSGVhcnQgYW5kIFZhc2N1bGFyIEluc3RpdHV0ZeKAmXMgRGlyZWN0IGFkZHJlc3MNCg0KLS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0NCk1JR2ZNQTBHQ1NxR1NJYjNEUUVCQVFVQUE0R05BRENCaVFLQmdRQysrM3RvczN4cTVhSWFKLzZSREd6REZKK2YNCjJNWkxHdHEyZXM5T1NRdEpzYU9YNjd6VlI5QnpMZWgwa2pMZ3ZOMC85Q0NxNDdQS3dvQWV4b2R2MXVhanF3YWcNCnBHYlV0NkF5ZHEzeE9LMllhRnkzTDVMMXBHc2NySzJPMXJSd0ExYUpndXdRVjArM0xYNmVwOExBVitkZFVaS3cNCjB4MlRyUkRZUUJFZE52YkFVd0lEQVFBQg0KLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0tDQo='
            },
            {
              'url' : 'expirationDate',
              'valueDate' : '2019-04-07'
            },
            {
              'url' : 'trustFramework',
              'valueCodeableConcept' : {
                'coding' : [
                  {
                    'system' : 'http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-digitalcertificate',
                    'code' : 'direct',
                    'display' : 'DirectTrust'
                  }
                ]
              }
            }
          ]
        }
      ],
      'status' : 'active',
      'connectionType' : {
        'system' : 'http://terminology.hl7.org/CodeSystem/endpoint-connection-type',
        'code' : 'direct-project',
        'display' : 'Direct Project'
      },
      'name' : r.endpoint[0].display,
      'managingOrganization' : {
        'reference' : r.organization.reference if r.organization.reference else f'Organization/{r.id}',
        'display' :  r.organization.display if r.organization.display else f'Organization/{r.name}'
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
      'address' : f'mailto:{slugify(r.practitioner.display if r.practitioner.display else r.contact.name.text)}'
                  f'@direct.{slugify(r.organization.display if r.organization.display else r.name)}.org'
    }


r = PR.PractitionerRole(r_dict)
print(r.resource_type)
print(attrgetter('practitioner.display')(r))

mo_map = dict(
PractitionerRole='organization',
Organization=f'Organization/{r.id}',
OrganizationAffiliation='organization',
Location='managingOrganization',
HealthcareService='providedBy'
)

print(mo_map[r.resource_type])
mo=getattr(r,mo_map[r.resource_type])
print(mo.reference)
print(mo.display)
#pprint(endpoint(r))

ep = EP.Endpoint(endpoint(r))

#print(dumps(ep.as_json(),indent=3, ensure_ascii=False))
