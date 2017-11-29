This profile sets minimum expectations for searching for and fetching information associated with a practitioner. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the practitioner resource when using this profile.

**Background & Scope**

A practitioner is a person who is directly or indirectly involved in the provisioning of healthcare.

This profile constrains the cardinality of a number of attributes of the practitioner resource such that they are required, including `practitioner.active`, `practitioner.name`, `practitioner.telecom`, `practitioner.address`, `practitioner.gender`, and `practitioner.birthDate`. It also adds a number of optional extensions to describe endpoints and digital certificates associated with a practitioner, accessibility options offered by a practitioner (e.g. cultural competence), and a practitioner's language proficiency.

**Examples:**

The following are example uses for the vhdir-practitioner profile:

-  TBD


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each practitioner must have:

1.  A boolean value in `practitioner.active`
1.  One name in `practitioner.name`
1.  At least one contact point associated with the practitioner in `practitioner.telecom`
1.  At least one address associated with the practitioner in `practitioner.address`
1.  A gender in `practitioner.gender`
1.  A birth date in `practitioner.birthDate`


**Profile specific implementation guidance:**

- TBD


**Extensions:**

1.  Restriction (0..*) - indicates restrictions on the use/release of information associated with the practitioner
1.  Endpoint (0..*) - reference(s) to the endpoint resource, indicating technical endpoints for the practitioner independent of their role at an organization
1.  Accessibility (0..*) - indicates accessibility options offered by the practitioner (e.g. cultural competence), consisting of:
    1.  Type (1..1) - indicates the type of accessibility option offered by the practitioner
    1.  Description (0..1) - additional descriptive information about the accessibility option
1.  Proficiency (0..1) - indicates a practitioner's level of proficiency with the language(s) specified in `practitioner.communication`
1.  DigitalCertificate (0..*) - a digital certificate associated with the practitioner


**Terminology**

TBD