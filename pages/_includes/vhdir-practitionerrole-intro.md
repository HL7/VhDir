This profile sets minimum expectations for searching for and fetching information associated with a practitioner role. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the practitionerRole resource when using this profile.

**Background & Scope**

PractitionerRole describes the role a practitioner plays at an organization, including the services they provide, the location(s) where they work, and their availability, electronic endpoints, and other relevant information.

This profile constrains the cardinality of the `practitionerRole.active` and `practitionerRole.code` attributes such that they are required. The profile also adds extensions to describe the healthcare provider insurance network(s) the practitioner participates in, qualifications pertaining to their role, whether the practitioner is accepting new patients in their role, and any digital certificates associated with their role.

**Examples:**

The following are example uses for the vhdir-practitionerRole profile:

-  [George Washington practices at Founding Fathers Memorial Hospital](PractitionerRole-practitionerrole1.html)


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each practitionerRole must have:

1.  A boolean value in `practitionerRole.active`
1.  At least one value describing the role the practitioner performs in `practitionerRole.code`


**Profile specific implementation guidance:**

- TBD


**Extensions:**

1.  [Network](StructureDefinition-network-reference.html) (0..*) - a reference to the healthcare provider insurance networks the practitioner participates in through their role
1.  [NewPatients](StructureDefinition-newpatients.html) (0..*) - indicates whether the practitioner is accepting new patients in their role
1.  [NewPatientProfile](StructureDefinition-newpatientprofile.html) (0..*) - a description of the type of new patients a practitioner accepts in their role (e.g. pediatric only)
1.  [Qualification](StructureDefinition-qualification.html) (0..*) - indicates qualifications the practitioner has through their role (e.g. registered to prescribe controlled substances)
1.  [DigitalCertificate](StructureDefinition-digitalcertificate.html) (0..*) - a digital certificate associated with the practitioner in their role


**Terminology**

TBD
