This profile sets minimum expectations for searching for and fetching information associated with an organization role. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the practitionerRole resource when using this profile.

**Background & Scope**

We propose the creation of a new organizationRole resource to describe relationships between two or more organizations. OrganizationRole describes the role an organization plays at an organization, including the services they provide, the location(s) where they provide services, and their availability, electronic endpoints, and other relevant information.

OrganizationRole addresses the need to define a non-hierarchical relationship between two or more organizations. For example:
*  One organization may provide services to another organization
*  Two or more organizations may form a partnership or joint venture
*  An organization may be a member of another organization, but not owned by it (e.g. a hospital is a member the American Hospital Association, a hospital is a member of a health information exchange network)

OrganizationRole is similar in form and function to practitionerRole. 

**Examples:**

The following are example uses for the vhdir-organizationRole profile:

-  TBD


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each organizationRole must have:

1.  A boolean value in `practitionerRole.active`
1.  At least one value describing the role the practitioner performs in `practitionerRole.code`
1.  For each indication of whether the practitioner is accepting new patients in thier role, one boolean value in `practitionerRole.newPatients.acceptingPatients` (extension)


**Profile specific implementation guidance:**

- TBD


**Extensions:**

1.  Restriction (0..*) - indicates restrictions on the use/release of information associated with an organization role


**Terminology**

TBD
