This profile sets minimum expectations for searching for and fetching information associated with an organization role. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the OrganizationAffiliation resource when using this profile.

**Background & Scope**

The OrganizationAffiliation resource describes relationships between two or more organizations, including the services one organization provides another, the location(s) where they provide services, the availability of those services, electronic endpoints, and other relevant information.

OrganizationAffiliation addresses the need to define a non-hierarchical relationship between two or more organizations. For example:
*  One organization may provide services to another organization
*  Two or more organizations may form a partnership or joint venture
*  An organization may be a member of another organization, but not owned by it (e.g. a hospital is a member the American Hospital Association, a hospital is a member of a health information exchange network)

OrganizationAffiliation is similar in structure to practitionerRole. Instead of references to practitioner and organization (as in practitionerRole), organizationaffiliation includes references to a participatingOrg and an organization. The participating organization provides "services" to the primary organization (much like a practitioner provides services to an organization). Using the three examples above:
*  The participating organization provides services to the primary organization
*  The joint venture is considered the primary organization, and partners within the joint venture are considered participating organizations (requires two organizationaffiliation resource instances)
*  An association is the primary organization, and its members are participating organizations.

OrganizationAffiliation is also used to indicate when an organization provides services for a health insurance provider network.

--

This profile modifies the base OrganizationAffiliation resource in the following manner:

*  Constrains the cardinality of `OrganizationAffiliation.active` (1..1), `OrganizationAffiliation.telecom.system` (1..1), and `OrganizationAffiliation.telecom.value` (1..1)

*  All references SHALL conform to the appropriate Validated Healthcare Directory Implementation Guide profile

*  Adds extensions:

1.  [Identifier status](StructureDefinition-identifier-status.html) (1..1) - indicates the status of an identifier for the role
1.  [Via intermediary](StructureDefinition-contactpoint-viaintermediary.html) (0..1) - a reference to an alternative point of contact for this role
1.  [Available time](StructureDefinition-contactpoint-availabletime.html) (0..*) - indicates when the point of contact for this role is available
1.  [Restriction](StructureDefinition-usage-restriction.html) (0..*) - indicates whether disclosure of any data associated with this role is restricted

<!--- *  Adds new value sets/updates value set bindings:

TBD --->
**Examples:**

The following are example uses for the vhdir-organizationaffiliation profile:

-  [Independence Rehabilitation provides rehab services to Founding Fathers Memorial Hospital](OrganizationAffiliation-orgrole1.html)
-  [Founding Fathers Memorial Hospital is a member of Monument HIE](OrganizationAffiliation-orgrole2.html)


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each OrganizationAffiliation must have:

1.  A boolean value in `OrganizationAffiliation.active`

<!--- **Profile specific implementation guidance:**

- TBD --->