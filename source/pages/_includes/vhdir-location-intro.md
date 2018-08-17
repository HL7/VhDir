This profile sets minimum expectations for searching for and fetching information associated with a location. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the Location resource when using this profile.

**Background & Scope**

A location is the physical place where healthcare services are provided, practitioners are employed, organizations are based, etc. Locations can range in scope from a room in a building to a geographic region/area.

This profile modifies the base Lractitioner resource in the following manner:

*  Constrains the cardinality of `location.status` (1..1), `location.operationalStatus` (0..0), `location.mode` (0..0), `location.telecom.system` (1..1), and `location.telecom.value` (1..1), 

*  All references SHALL conform to the appropriate Validated Healthcare Directory Implementation Guide profile

*  Adds extensions:

1.  [Identifier status](StructureDefinition-identifier-status.html) (1..1) - indicates the status of a location's identifier
1.  [Via intermediary](StructureDefinition-contactpoint-viaintermediary.html) (0..1) - a reference to an alternative point of contact for this location
1.  [Available time](StructureDefinition-contactpoint-availabletime.html) (0..*) - indicates when a location is available for contact
1.  [Boundary](StructureDefinition-boundary.html) (0..*) - indicates a region/area for the location
1.  [Accessibility](StructureDefinition-accessibility.html) (0..*) - indicates accessibility options available at the location (e.g. handicap accessibility)
1.  [EHR](StructureDefinition-ehr.html) (0..*) - provides information about the EHR product(s) used at the location
1.  [NewPatients](StructureDefinition-newpatients.html) (0..*) - indicates whether the location is accepting new patients
1.  [NewPatientProfile](StructureDefinition-newpatientprofile.html) (0..*) - a description of the type of patients the location accepts (e.g. pediatric only)
1.  [Restriction](StructureDefinition-usage-restriction.html) (0..*) - indicates whether disclosure of any data associated with a location is restricted

*  Adds new value sets/updates value set bindings:

TBD



**Examples:**

The following are example uses for the vhdir-location profile:

-  [Founding Fathers Memorial Hospital, Main Campus](Location-loc-ffmh.html)


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.

Each Location must have: 

1.  One coded value in `location.status`


**Profile specific implementation guidance:**

- TBD

