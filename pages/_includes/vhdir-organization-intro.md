This profile sets minimum expectations for searching for and fetching information associated with an organization. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the Organization resource when using this profile.

**Background & Scope**

An organization is a formal or informal grouping of people or organizations with a common purpose, such as a company, institution, corporation, community group, or healthcare practice. 

This profile constrains the cardinality of `organization.name`, `organization.type`, and `organization.active` (all are required). It also includes optional extensions representing additional information about an organization's alias(es), a description of the organization, an organization's qualifications (e.g. accreditations), and digital certificates for the organization.

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


**Extensions:**

1.  [Alias type](StructureDefinition-org-alias-type.html) (0..1) - indicates whether an organization's alias is a historical name or legal alternative name
1.  [Alias period](StructureDefinition-org-alias-period.html) (0..1) - indicates a period of time for which an organization used an alias
1.  [Description](StructureDefinition-org-description.html) (0..1) - a friendly description of the organization
1.  [Qualification](StructureDefinition-qualification.html) (0..*) - indicates whether the organization has any formal qualifications 
1.  [DigitalCertificate](StructureDefinition-digitalcertificate.html) (0..*) - a digital certificate associated with the organization


**Terminology**

TBD