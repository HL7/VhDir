#### Complete Summary of the Mandatory Requirements

There are no mandatory attributes for the location resource. However, some attributes have mandatory components if they are included in the resource (including extensions):

1.  If the location has a defined position, one value representing longitude in `location.position.longitude` and one value representing latitude in `location.position.latitude`
1.  If the location has a geographic region/area, one URI to a KML or GeoJSON object defining the region/area in `location.boundary.region` (extension)
1.  For each accessibility option offered by the location, one type in `location.accessibility.type` (extension)
1.  For each indication of whether the location is accepting new patients, one boolean value in `location.newPatients.acceptingPatients` (extension)
1.  For each indication that the location is not available, a description of why the location is unavailable in `location.notAvailable.description` (extension)
