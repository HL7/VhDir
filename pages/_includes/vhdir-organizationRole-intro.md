This profile sets minimum expectations for searching for and fetching information associated with an organization role. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the organizationRole resource when using this profile.

**Background & Scope**

We propose the creation of a new organizationRole resource to describe relationships between two or more organizations. OrganizationRole describes the role an organization plays at an organization, including the services they provide, the location(s) where they provide services, and their availability, electronic endpoints, and other relevant information.

OrganizationRole addresses the need to define a non-hierarchical relationship between two or more organizations. For example:
*  One organization may provide services to another organization
*  Two or more organizations may form a partnership or joint venture
*  An organization may be a member of another organization, but not owned by it (e.g. a hospital is a member the American Hospital Association, a hospital is a member of a health information exchange network)

OrganizationRole is similar in form and function to practitionerRole. Instead of references to practitioner and organization (as in practitionerRole), organizationRole includes references to a participatingOrg and a primaryOrg. The participating organization provides "services" to the primary organization (much like a practitioner provides services to an organization). Using the three examples above:
*  The participating organization provides services to the primary organization
*  The joint venture is considered the primary organization, and partners within the joint venture are considered participating organizations
*  An association is the primary organization, and its members are participating organizations.

As with practitionerRole, organizationRole provides the link between an organization and a health insurance provider network.

**Examples:**

The following are example uses for the vhdir-organizationRole profile:

-  TBD


**Mandatory Data Elements**

No mandatory elements in the proposed organizationRole Resource. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements. 



**Profile specific implementation guidance:**

- TBD


**Terminology**

TBD
