from datetime import datetime
from json import dumps
from fhirr4models import location as L
from string import punctuation
from stringcase import spinalcase, titlecase, snakecase


timestamp = f'{datetime.utcnow().isoformat()}Z'



# ********* Location for Coverage Location ********************

def get_coverage(loc_data):
    return {
  'resourceType' : 'Location',
  'id' : loc_data["id"],
  'meta' : {
    'profile' : [
      'http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-location'
    ]
  },
  'extension' : [

{
    'url' : 'http:#hl7.org/fhir/StructureDefinition/location-boundary-geojson',  # R!
    'valueAttachment' : loc_data["attachment"]  # Value of extension
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
      'value' : loc_data["name"].lower()
      }
  ],
  'status' : 'active',
  'name' : loc_data["name"],
  'description' : f'Coverage Area for {loc_data["name"]}',
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

def slugify(s):
    for c in punctuation:
        s= s.replace(c,'')
    s = s.lower()
    s = spinalcase(s)
    return s

states = ['Massachusetts','Connecticut','Rhode Island']
for state in states:
    loc_data = dict (
    id = f'vhdir-coverage-location-{slugify(state)}',
    name = state,
    attachment = {
      'contentType' : 'application/vnd.geo+json',  # Mime type of the content, with charset etc.
      'data' : '<base64Binary>',  # Data inline, base64ed
      'title' : f'GeoJSON for {state}',  # Label to display in place of the data
      'creation' : timestamp  # Date attachment was first created
    }
    )

    coverage = get_coverage(loc_data)

    location = L.Location(coverage)
    print(dumps(location.as_json(),indent=3))
    print(location.extension[0].as_json())
