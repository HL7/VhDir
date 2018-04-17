This profile sets minimum expectations for searching for and fetching information associated with an organization. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the Organization resource when using this profile.

**Background & Scope**

An organization is a formal or informal grouping of people or organizations with a common purpose, such as a company, institution, corporation, community group, or healthcare practice. 

This profile modifies the base Organization resource in the following manner:

*  Constrains the cardinality of `organization.active` (1..1), `organizaton.type` (1..*), `organization.name` (1..1), `organization.telecom.system` (1..1), `organization.telecom.value` (1..1), `organization.contact.name.family` (1..1), `organization.contact.name.given` (1..*), `organization.contact.telecom.system` (1..1), and `organization.contact.telecom.value` (1..1)

*  Adds extensions:

1.  [Identifier status](StructureDefinition-identifier-status.html) (1..1) - indicates the status of an organization's identifier
1.  [Via intermediary](StructureDefinition-contactpoint-viaintermediary.html) (0..1) - a reference to an alternative point of contact for this organization
1.  [Available time](StructureDefinition-contactpoint-availabletime.html) (0..*) - indicates when an organization is available for contact
1.  [Geolocation](http://hl7.org/fhir/StructureDefinition/geolocation) (0..1) - indicates the absolute geographic location of an organization's address
1.  [Alias type](StructureDefinition-org-alias-type.html) (0..1) - indicates whether an organization's alias is a historical name or legal alternative name
1.  [Alias period](StructureDefinition-org-alias-period.html) (0..1) - indicates a period of time for which an organization used an alias
1.  [Description](StructureDefinition-org-description.html) (0..1) - a friendly description of the organization
1.  [Qualification](StructureDefinition-qualification.html) (0..*) - indicates whether the organization has any formal qualifications 
1.  [DigitalCertificate](StructureDefinition-digitalcertificate.html) (0..*) - a digital certificate associated with the organization
1.  [Restriction](StructureDefinition-usage-restriction.html) (0..*) - indicates whether disclosure of any data associated with an organization is restricted

*  Adds new value sets/updates value set bindings:

TBD


**Examples:**

The following are example uses for the vhdir-organization profile:

-  [Founding Fathers Memorial Hospital](Organization-foundingfathers.html)


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each organization must have:

1.  A boolean value in `organization.active`
1.  A name in `organization.name`
1.  A type in `organization.type`


**Profile specific implementation guidance:**

- TBD
