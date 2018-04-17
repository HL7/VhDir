This profile sets minimum expectations for searching for and fetching information associated with a practitioner role. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the PractitionerRole resource when using this profile.

**Background & Scope**

PractitionerRole describes the role a practitioner plays at an organization, including the services they provide, the location(s) where they work, and their availability, electronic endpoints, and other relevant information.

This profile modifies the base PractitionerRole resource in the following manner:

*  Constrains the cardinality of `practitionerRole.active` (1..1) and `practitionerRole.code` (1..*)

*  Adds extensions:

1.  [Identifier status](StructureDefinition-identifier-status.html) (1..1) - indicates the status of a practitionerRole's identifier
1.  [Via intermediary](StructureDefinition-contactpoint-viaintermediary.html) (0..1) - a reference to an alternative point of contact for a practitioner in a role
1.  [Available time](StructureDefinition-contactpoint-availabletime.html) (0..*) - indicates when the contact point for a practitioner in a role is available
1.  [Network](StructureDefinition-network-reference.html) (0..*) - a reference to the healthcare provider insurance networks the practitioner participates in through their role
1.  [NewPatients](StructureDefinition-newpatients.html) (0..*) - indicates whether the practitioner is accepting new patients in their role
1.  [NewPatientProfile](StructureDefinition-newpatientprofile.html) (0..*) - a description of the type of new patients a practitioner accepts in their role (e.g. pediatric only)
1.  [Qualification](StructureDefinition-qualification.html) (0..*) - indicates qualifications the practitioner has through their role (e.g. registered to prescribe controlled substances)
1.  [DigitalCertificate](StructureDefinition-digitalcertificate.html) (0..*) - a digital certificate associated with the practitioner in their role
1.  [Restriction](StructureDefinition-usage-restriction.html) (0..*) - indicates whether disclosure of any data associated with a practitionerRole is restricted

*  Adds new value sets/updates value set bindings:

TBD


**Examples:**

The following are example uses for the vhdir-practitionerrole profile:

-  [George Washington practices at Founding Fathers Memorial Hospital](PractitionerRole-practitionerrole1.html)


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each practitionerRole must have:

1.  A boolean value in `practitionerRole.active`
1.  At least one value describing the role the practitioner performs in `practitionerRole.code`


**Profile specific implementation guidance:**

- TBD
