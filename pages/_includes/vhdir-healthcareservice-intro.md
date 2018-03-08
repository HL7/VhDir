This profile sets minimum expectations for searching for and fetching information associated with a healthcare service. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the healthcareService resource when using this profile.

**Background & Scope**

The healthcareService resource typically describes services offered by an organization at a location. The resource may be used to encompass a variety of services covering the entire healthcare spectrum, including promotion, prevention, diagnstics, hospital and ambulatory care, home care, long-term care, and other health-related and community services.

This profile makes relatively few changes to the base FHIR resource. It adds an extension to represent the coverage area of a service, rather than using a reference to a location resource in `healthcareService.coverageArea` (because the location resource only represents a defined point, rather than a geographic area/region). It also includes optional extensions to describe whether the service is accepting new patients.

**Examples:**

The following are example uses for the vhdir-healthcareService profile:

-  TBD


**Mandatory Data Elements**

There are no mandatory attributes for the healthcareService resource. However, some attributes have mandatory components if they are included in the resource (including extensions). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  


1.  For each indication of when a service is not available, a description of why the service is unavailable in `healthcareService.notAvailable.description`
1.  For each geographic area described for the service, one URI to a KML or GeoJSON object defining the region/area in `healthcareService.boundary.region` (extension)
1.  For each indication of whether the service is accepting new patients, one boolean value in `healthcareService.newPatients.acceptingPatients` (extension)


**Profile specific implementation guidance:**

- TBD


**Extensions:**

1.  Boundary (0..*) - indicates a region/area in which the service is available, consisting of:
    1. Region (1..1) - a URI to a KML or GeoJSON object defining the region/area
    1. LocalName (0..*) - a friendly description of the region/area (such as the colloquial name of the region)
1.  NewPatients (0..*) - indicates whether the service is accepting new patients, consisting of:
    1.  AcceptingPatients (1.1) - a value of 'true' means the service is accepting new patients, 'false' means it is not
    1.  Network (0..1) - indicates whether the service is accepting new patients for a particular health provider insurance network
1.  NewPatientProfile (0..1) - a description of the type of patients the service accepts (e.g. pediatric only)


**Terminology**

TBD
