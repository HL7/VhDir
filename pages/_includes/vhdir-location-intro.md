This profile sets minimum expectations for searching for and fetching information associated with a location. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the location resource when using this profile.

**Background & Scope**

A location is the physical place where healthcare services are provided, practitioners are employed, organizations are based, etc. Locations can range in scope from a room in a building to a geographic region/area.

This profile removes `location.operationalStatus` because maintaining bed-level information is out of scope for this implementation guide. It also removes `location.mode` because maintaining information about kinds of locations (as opposed to actual location instances) is out of scope for this implementation guide. 

This profile also adds a number of optional extensions, including extensions for representing a geographic region/area, accessibility options at the location, the EHR product(s) in use at the location, and whether the location is accepting new patients.

**Examples:**

The following are example uses for the vhdir-location profile:

-  TBD


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.

Each Location must have: 

1.  One coded value in `location.status`


**Profile specific implementation guidance:**

- TBD


**Extensions:**

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


**Terminology**

TBD
