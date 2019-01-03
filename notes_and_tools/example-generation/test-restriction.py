def restriction(data):

    return {
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
      'action' : [
        {
          'system' : 'http://terminology.hl7.org/CodeSystem/v3-ActReason', # Identity of the terminology system
          'code' : 'use',
          'display' : 'Use'
        }
      ],
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
