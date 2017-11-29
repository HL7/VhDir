This profile sets minimum expectations for searching for and fetching information associated with an organization. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the organization resource when using this profile.

**Background & Scope**

An organization is a formal or informal grouping of people or organizations with a common purpose, such as a company, institution, corporation, community group, or healthcare practice. 

This profile constrains the cardinality of `organization.name`, `organization.type`, and `organization.active` (all are required). It also adds optional extensions to represent more information about an organization's alias(es), a description of the organization, the organization's qualifications (e.g. accreditations), and digital certificates for the organization.

**Examples:**

The following are example uses for the vhdir-organization profile:

-  TBD


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each organization must have:

1.  A boolean value in `organization.active`
1.  A name in `organization.name`
1.  A type in `organization.type`
1.  For each alias, a name in `organization.alias.name`


**Profile specific implementation guidance:**

- TBD


**Extensions:**

1.  Restriction (0..*) - indicates restrictions on the use/release of information associated with the organization
1.  Alias (0..*) - a list of other names the organization is known by, consisting of:
    1.  Name (1..1) - the alias
    1.  Type (0..1) - indicates the type of alias
    1.  Period (0..1) - indicates the period during which the alias is in use
1.  Description (0..1) - a friendly description of the organization
1.  Qualification (0..*) - indicates whether the organization has any formal qualifications
1.  DigitalCertificate (0..*) - a digital certificate associated with the organization


**Terminology**

TBD