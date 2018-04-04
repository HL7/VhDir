This profile sets minimum expectations for searching for and fetching information associated with a healthcare provider insurance network. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the Organization resource when using this profile.

**Background & Scope**

A network refers to a healthcare provider insurance network. A healthcare provider insurance network is an aggregation of organizations and individuals that deliver a set of services across a geography through health insurance products/plans. A network is typically owned by a payer.

Network is a profile on the Organization resource. This profile constrains the cardinality of `organization.active` and `organization.partOf` such that they are both required, and removes the `organization.telecom` element. It changes the value set for `organization.type` to a more appropriate value set enumerating types of healthcare provider insurance networks. Finally, it adds extensions to represent a time period for the network and a coverage area for the network (via a reference to a location resource).

**Examples:**

The following are example uses for the vhdir-network profile:

-  [Patriot Preferred Provider Network](Organization-patriotppo.html)


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each network must have:

1.  A coded value in `organization.active`
1.  A reference to an organization or organizationRole resource indicating the owner of the network in `organization.partOf`


**Profile specific implementation guidance:**

- TBD


**Extensions:**

1.  [Period](http://hl7.org/fhir/StructureDefinition/organization-period) (0..1) - Represents a time period for the network
1.  [Coverage area](StructureDefinition-location-reference.html) (0..*) - Indicates a coverage area for the network


**Terminology**

TBD
