This profile sets minimum expectations for searching for and fetching information associated with a location. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the location resource when using this profile.

**Background & Scope**

A location is the physical place where healthcare services are provided, practitioners are employed, organizations are based, etc. Locations can range in scope from a room in a building to a geographic region/area.

This profile removes `location.operationalStatus` because maintaining bed-level information is out of scope for this implementation guide. It also removes `location.mode` because maintaining information about kinds of locations (as opposed to actual location instances) is out of scope for this implementation guide. 

This profile also adds a number of optional extensions, including extensions for representing a geographic region/area, accessibility options at the location, the EHR product(s) in use at the location, whether the location is accepting new patients, and when the location is available.

**Examples:**

The following are example uses for the vhdir-location profile:

-  TBD


**Mandatory Data Elements**

There are no mandatory attributes for the healthcareService resource. However, some attributes have mandatory components if they are included in the resource (including extensions). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.   


1.  If the location has a defined position, one value representing longitude in `location.position.longitude` and one value representing latitude in `location.position.latitude`
1.  If the location has a geographic region/area, one URI to a KML or GeoJSON object defining the region/area in `location.boundary.region` (extension)
1.  For each accessibility option offered by the location, one type in `location.accessibility.type` (extension)
1.  For each indication of whether the location is accepting new patients, one boolean value in `location.newPatients.acceptingPatients` (extension)
1.  For each indication that the location is not available, a description of why the location is unavailable in `location.notAvailable.description` (extension)


**Profile specific implementation guidance:**

- TBD


**Extensions:**

1.  Restriction (0..*) - indicates restrictions on the use/release of information associated with the location
1.  Boundary (0..*) - indicates a region/area for the location, consisting of:
    1. Region (1..1) - a URI to a KML or GeoJSON object defining the region/area
    1. LocalName (0..*) - a friendly description of the region/area (such as the colloquial name of the region)
1.  Accessibility (0..*) - indicates accessibility options available at the location (e.g. handicap accessibility), consisting of:
    1.  Type (1..1) - indicates the type of accessibility option offered at the location
    1.  Description (0..1) - additional descriptive information about the accessibility option
1.  EHR (0..*) - provides information about the EHR product(s) used at the location, consisting of:
    1.  Developer (0..1) - the developer of the EHR product
    1.  Product (0..1) - the name of the EHR product
    1.  Version (0..1) - the version of the EHR product
    1.  CertificationID (0..1) - a unique ID assigned by the ONC-Authorized Certification Body
    1.  CertificationEdition (0..1) - indicates which certification edition the EHR product has been certified to
    1.  PatientAccess (0..*) - indicates whether the EHR product provides patient access functions (e.g. a patient portal)
1.  NewPatients (0..*) - indicates whether the location is accepting new patients, consisting of:
    1.  AcceptingPatients (1.1) - a value of 'true' means the location is accepting new patients, 'false' means it is not
    1.  Network (0..1) - indicates whether the location is accepting new patients for a particular health provider insurance network
1.  NewPatientProfile (0..1) - a description of the type of patients the location accepts (e.g. pediatric only)
1.  AvailableTime (0..*) - indicates when the location is available, consisting of:
    1.  DaysOfWeek (0..*) - indicates the days the location is available
    1.  AllDay (0..1) - indicates whether the location is always available
    1.  AvailableStartTime (0..1) - indicates when the location opens
    1.  AvailableEndTime (0..1) - indicates when the location closes
1.  NotAvailable (0..*) - indicates when the location is not available
    1.  Description (1..1) - describes why the location is not available
    1.  During (0..1) - indicates a period of time for when the location is not available
1.  AvailabilityExceptions (0..1) - indicates any exceptions to the availablity of the location    


**Terminology**

TBD
