This profile sets minimum expectations for searching for and fetching information associated with a healthcare provider insurance network. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the Organization resource when using this profile.

**Background & Scope**

A network refers to a healthcare provider insurance network. A healthcare provider insurance network is an aggregation of organizations and individuals that deliver a set of services across a geography through health insurance products/plans. A network is typically owned by a payer.

Network is a profile on the Organization resource. This profile modifies the base Organization resource in the following manner:

*  Constrains the cardinality of `organization.active` (1..1), `organization.telecom` (0..0), `organization.partOf` (1..1), `organization.contact.name.family` (1..1), `organization.contact.name.given` (1..*), `organization.contact.telecom.system` (1..1), and `organization.contact.telecom.value` (1..1)

*  All references SHALL conform to the appropriate Validated Healthcare Directory Implementation Guide profile

*  Adds extensions:

1.  [Identifier status](StructureDefinition-identifier-status.html) (1..1) - indicates the status of an organization's identifier
1.  [Via intermediary](StructureDefinition-contactpoint-viaintermediary.html) (0..1) - a reference to an alternative point of contact for this organization
1.  [Available time](StructureDefinition-contactpoint-availabletime.html) (0..*) - indicates when an organization is available for contact
1.  [Geolocation](http://hl7.org/fhir/StructureDefinition/geolocation) (0..1) - indicates the absolute geographic location of an organization's address
1.  [Period](http://hl7.org/fhir/StructureDefinition/organization-period) (0..1) - Represents a time period for the network
1.  [Coverage area](StructureDefinition-location-reference.html) (0..*) - Indicates a coverage area for the network
1.  [Restriction](StructureDefinition-usage-restriction.html) (0..*) - indicates whether disclosure of any data associated with a network is restricted

*  Adds new value sets/updates value set bindings:

TBD



**Examples:**

The following are example uses for the vhdir-network profile:

-  [Patriot Preferred Provider Network](Organization-patriotppo.html)


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each network must have:

1.  A coded value in `organization.active`
1.  A reference to an organization or organizationaffiliation resource indicating the owner of the network in `organization.partOf`


**Profile specific implementation guidance:**

- TBD
