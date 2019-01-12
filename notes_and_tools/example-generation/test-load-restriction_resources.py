restriction = {
    'resourceType' : 'Consent',
    'id' : 'restrict',
    'meta' : {
      'profile' : [
        'http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-restriction'
      ]
    },
    'status' : 'active',
    'scope' : {
        'coding': [{
          'system' : 'http://terminology.hl7.org/CodeSystem/consentscope',
          'code' : 'patient-privacy',
          'display' : 'Privacy Consent'
}]    },
    'category' : [
    {
        'coding': [{
          'system' : 'http://terminology.hl7.org/CodeSystem/v3-ActCode',
          'code' : 'INFA',
          'display' : 'information access'
        }]
        }
    ],
    'dateTime' : '2017-12-18',
    'policy' : [
      {
        'uri' : 'http://example.org/federal/policy#womans-shelter'
      }
    ],
    'provision' : {
      'type' : 'permit',
      'actor' : [
        {
          'role' : {
            'coding' : [
              {
                'system' : 'http://terminology.hl7.org/CodeSystem/v3-ParticipationType',
                'code' : 'IRCP',
                'display' : 'information recipient'
              }
            ]
          },
          'reference' : {
            'display' : 'Blue Team @ The W shelter (CareTeam)'
          }
        }
      ],
      'action' : [{
      'coding' : [
        {
          'system' : 'http://terminology.hl7.org/CodeSystem/v3-ActReason', # Identity of the terminology system
          'code' : 'use',
          'display' : 'Use'
        }]
      }],
      'securityLabel' : [
        {
          'system' : 'http://terminology.hl7.org/CodeSystem/v3-ActCode', # Identity of the terminology system
          'code' : 'SDV',
          'display' : 'sexual assault, abuse, or domestic violence information sensitivity'
      }
      ],
      'purpose' : [
        {
           'system' : 'http://terminology.hl7.org/CodeSystem/v3-ActReason', # Identity of the terminology system
          'code' : 'TREAT',
          'display' : 'treatment'
        }
      ]
    }
  }


hcs = {
    'resourceType': 'HealthcareService',
    'id': 'vhdir-miscellaneous-healthcareservice-9994427431',
    'meta': {
        'profile': [
            'http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-healthcareservice'
        ]
    },
    'contained':[
    restriction
  ],
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
                        'code': 'PRN'
                    }
                ],
                'text': 'Healthcare Service Number'
            },
            'system': 'https://essent-healthcare--ayer-inc.com',
            'value': '9994427431-miscellaneous',
            'assigner': {
                'reference': 'Organization/vhdir-organization-9994427431',
                'display': 'ESSENT HEALTHCARE - AYER, INC.'
            }
        }
    ],
    'active': True,
    'providedBy': {
        'reference': 'Organization/vhdir-organization-9994427431',
        'display': 'ESSENT HEALTHCARE - AYER, INC.'
    },
    'type': [
        {
            'coding': [
                {
                    'system': 'http://https://essent-healthcare--ayer-inc.com/service-types',
                    'code': 'miscellaneous',
                    'display': 'MISCELLANEOUS'
                }
            ],
            'text': 'MISCELLANEOUS'
        }
    ],
    'specialty': [
        {
            'coding': [
                {
                    'system': 'http://nucc.org/provider-taxonomy',
                    'code': 'miscellaneous',
                    'display': 'Miscellaneous'
                }
            ],
            'text': 'Miscellaneous'
        }
    ],
    'location': [{
    'extension' : [
       {
         'url' : 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/usage-restriction',
         'valueReference' : {
           'reference' : '#restrict'
         }
       }
     ],

        'reference' : 'Location/loc-ws',
      'display' : 'The W Womens Shelter'
        }
    ],
    'name': "Middelsex County Women's Shelter",
    'comment': "This is an example of a Women's shelter to demonstrate how to restrict multiple contents",
    'telecom': [
        {
        "extension" : [
        {
          "url" : "http://hl7.org/fhir/uv/vhdir/StructureDefinition/usage-restriction",
          "valueReference" : {
            "reference" : "#restrict"
          }
        }
      ],
            'system': 'phone',
            'value': '9787849000',
            'use': 'work',
            'rank': 1
        }
    ],
    'serviceProvisionCode': [
        {
            'coding': [
                {
                    'system': 'http://terminology.hl7.org/CodeSystem/service-provision-conditions',
                    'code': 'cost',
                    'display': 'Fees apply'
                }
            ]
        }
    ],
    'referralMethod': [
        {
            'coding': [
                {
                    'system': 'http://terminology.hl7.org/CodeSystem/service-referral-method',
                    'code': 'phone',
                    'display': 'phone'
                }
            ]
        },
        {
            'coding': [
                {
                    'system': 'http://terminology.hl7.org/CodeSystem/service-referral-method',
                    'code': 'fax',
                    'display': 'Fax'
                }
            ]
        }
    ],
    'appointmentRequired': True,
    'availableTime': [
        {
            'daysOfWeek': [
                'mon',
                'tue',
                'wed',
                'thu',
                'fri',
                'sat',
                'sun'
            ],
            'allDay': True
        }
    ],
    'endpoint': [
        {
            'reference': 'Endpoint/vhdir-miscellaneous-healthcareservice-9994427431-direct',
            'display': 'Direct address for ESSENT HEALTHCARE - AYER, INC. Shelter Counseling Service'
        }
    ]
}

ct = {
      'resourceType' : 'CareTeam',
      'id' : 'ws-blue-team',
      'meta' : {
        'profile' : [
          'http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-careteam'
        ]
      },
      'extension' : [
        {
          'url' : 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/careteam-alias',
          'valueString' : 'Blue Team @ The W shelter'
        },
        {
          'url' : 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/location-reference',
          'valueReference' : {
            'reference' : 'Location/loc-ws',
            'display' : 'The W shelter'
          }
        },
        {
          'url' : 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/healthcareservice-reference',
          'valueReference' : {
            'reference' : 'HealthcareService/vhdir-miscellaneous-healthcareservice-9994427431',
            'display' : 'ESSENT HEALTHCARE - AYER, INC. Miscellaneous Healthcare Service'
          }
        },
        {
          'url' : 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/endpoint-reference',
          'valueReference' : {
            'reference' : 'Endpoint/vhdir-careteam-9994427431-1-direct',
            'display' : 'Direct address for ESSENT HEALTHCARE - AYER, INC. Shelter Counseling Service'
          }
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
          'type' : {
            'coding' : [
              {
                'system' : 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'code' : 'PRN',
                'display' : 'Provider number'
              }
            ],
            'text' : 'Business ID'
          },
          'system' : 'http://example.org/www.foundingfathersmemorial.com',
          'value' : 'careteam0021',
          'period' : {
            'start' : '2018-07-16T09:00:00-05:00'
          }
        }
      ],
      'status' : 'active',
      'category' : [
        {
          'coding' : [
            {
              'system' : 'http://loinc.org',
              'code' : 'LA28866-4',
              'display' : 'Home & Community Based Services (HCBS)-focused care team'
            }
          ]
        }
      ],
      'name' : 'ESSENT HEALTHCARE WS Care Team',
      'period' : {
        'start' : '2018-07-16'
      },
      'participant' : [
        {
          'role' : [
            {
              'coding' : [
                {
                  'system' : 'http://nucc.org/provider-taxonomy',
                  'code' : '103TC1900X',
                  'display' : 'Psychologist/Counseling'
                }
              ]
            }
          ],
          'member' : {
            'reference' : 'PractitionerRole/vhdir-practitionerrole-9991891700-1',
            'display' : 'Counseling'
          },
          'period' : {
            'start' : '2018-07-16'
          }
        }
      ],
      'managingOrganization' : [
        {
          'reference' : 'Organization/vhdir-organization-9994427431',
          'display' : 'ESSENT HEALTHCARE - AYER, INC.'
        }
      ],
      'telecom' : [
        {
          'system' : 'phone',
          'value' : '4135862960',
          'use' : 'work'
        }
      ],
      'note' : [
        {
          'text' : 'This care team provides counseling services to the WS'
        }
      ]
    }

loc = {
  'resourceType' : 'Location',
  'id' : 'loc-ws',
  'meta' : {
    'profile' : [
      'http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-location'
    ]
  },
  'contained':[
  restriction
],
  'status' : 'active',
  'name' : 'The W Womens Shelter',
  'telecom' : [
    {
      'system' : 'url',
      'value' : 'https://exmaple.org/The-W-shelter'
    },
    {
      'extension' : [
        {
          'url' : 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/usage-restriction',
          'valueReference' : {
            'reference' : '#restrict'
          }
        }
      ],
      'system' : 'phone',
      'value' : '555 administration'
    }
  ],
  'address' : {
    'extension' : [
      {
        'url' : 'http://hl7.org/fhir/uv/vhdir/StructureDefinition/usage-restriction',
        'valueReference' : {
          'reference' : '#restrict'
        }
      }
    ],
    'line' : [
      '3300 Barnum Road'
    ],
    'city' : 'Ayer',
    'state' : 'MA',
    'postalCode' : '01432',
    'country' : 'USA'
  }
}


from json import dumps
from requests import put

headers ={
'Content-Type':'application/fhir+json',
'Accept':'application/fhir+json'
}

#in_path ='/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/sample-nppes-data'
#out_path = '/Users/ehaas/Documents/FHIR/VhDir/notes_and_tools/example-generation/examples'
#server_path = 'http://vhdir-demo.fhir.org/fhir'
server_path = 'http://wildfhir.aegis.net/fhir3-5-0'

examples = [hcs,ct,loc]


for example in examples:
    print(dumps(example,ensure_ascii=False))
    r = put(url=f'{server_path}/{example["resourceType"]}/{example["id"]}', data=dumps(example,ensure_ascii=False), headers=headers)
    print(f'put json status_code = {r.status_code}')
    if r.status_code >= 300:
        print(f'response as json = \n{dumps(r.json(), indent =3)}')
