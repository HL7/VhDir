This profile sets minimum expectations for searching for and fetching information associated with a location. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the location resource when using this profile.

**Background & Scope**

A location is the physical place where healthcare services are provided, practitioners are employed, organizations are based, etc. Locations can range in scope from a room in a building to a geographic region/area.

This profile removes `location.operationalStatus` because maintaining bed-level information is out of scope for this implementation guide. It also removes `location.mode` because maintaining information about kinds of locations (as opposed to actual location instances) is out of scope for this implementation guide. 

This profile also adds a number of optional extensions, including extensions for representing a geographic region/area, accessibility options at the location, the EHR product(s) in use at the location, and whether the location is accepting new patients.

**Examples:**

The following are example uses for the vhdir-location profile:

-  [Founding Fathers Memorial Hospital, Main Campus](Location-hospital1.html)


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.

Each Location must have: 

1.  One coded value in `location.status`


**Profile specific implementation guidance:**

- TBD


**Extensions:**

1.  [Boundary](StructureDefinition-boundary.html) (0..*) - indicates a region/area for the location
1.  [Accessibility](StructureDefinition-accessibility.html) (0..*) - indicates accessibility options available at the location (e.g. handicap accessibility)
1.  [EHR](StructureDefinition-ehr.html) (0..*) - provides information about the EHR product(s) used at the location
1.  [NewPatients](StructureDefinition-newpatients.html) (0..*) - indicates whether the location is accepting new patients
1.  [NewPatientProfile](StructureDefinition-newpatientprofile.html) (0..*) - a description of the type of patients the location accepts (e.g. pediatric only)


**Terminology**

TBD
