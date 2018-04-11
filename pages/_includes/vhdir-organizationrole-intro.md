This profile sets minimum expectations for searching for and fetching information associated with an organization role. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the OrganizationRole resource when using this profile.

**Background & Scope**

The OrganizationRole resource describes relationships between two or more organizations, including the services one organization provides another, the location(s) where they provide services, the availability of those services, electronic endpoints, and other relevant information.

OrganizationRole addresses the need to define a non-hierarchical relationship between two or more organizations. For example:
*  One organization may provide services to another organization
*  Two or more organizations may form a partnership or joint venture
*  An organization may be a member of another organization, but not owned by it (e.g. a hospital is a member the American Hospital Association, a hospital is a member of a health information exchange network)

OrganizationRole is similar in form and function to practitionerRole. Instead of references to practitioner and organization (as in practitionerRole), organizationRole includes references to a participatingOrg and an organization. The participating organization provides "services" to the primary organization (much like a practitioner provides services to an organization). Using the three examples above:
*  The participating organization provides services to the primary organization
*  The joint venture is considered the primary organization, and partners within the joint venture are considered participating organizations (requires two organizationRole resource instances)
*  An association is the primary organization, and its members are participating organizations.

OrganizationRole is also used to indicate when an organization provides services for a health insurance provider network.

**Examples:**

The following are example uses for the vhdir-organizationRole profile:

-  [Independence Rehabilitation provides rehab services to Founding Fathers Memorial Hospital](OrganizationRole-orgrole1.html)
-  [Founding Fathers Memorial Hospital is a member of Monument HIE](OrganizationRole-orgrole2.html)


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each OrganizationRole must have:

1.  A boolean value in `organizationRole.active`


**Profile specific implementation guidance:**

- TBD


**Terminology**

TBD
