#### Complete Summary of the Mandatory Requirements

There are no mandatory attributes for the healthcareService resource. However, some attributes have mandatory components if they are included in the resource (including extensions):

1.  For each indication of when a service is not available, a description of why the service is unavailable in `healthcareService.notAvailable.description`
1.  For each geographic area described for the service, one URI to a KML or GeoJSON object defining the region/area in `healthcareService.boundary.region` (extension)
1.  For each indication of whether the service is accepting new patients, one boolean value in `healthcareService.newPatients.acceptingPatients` (extension)
