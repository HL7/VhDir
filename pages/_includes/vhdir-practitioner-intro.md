This profile sets minimum expectations for searching for and fetching information associated with a practitioner. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the practitioner resource when using this profile.

**Background & Scope**

A practitioner is a person who is directly or indirectly involved in the provisioning of healthcare.

This profile constrains the cardinality of a few attributes of the practitioner resource such that they are required, including `practitioner.active` and `practitioner.name`. It also adds optional extensions to describe endpoints and digital certificates associated with a practitioner, accessibility options offered by a practitioner (e.g. cultural competence), a practitioner's spoken language proficiency, and additional information about their qualifications (i.e. where the qualification is valid and current/historical information about the qualification's status).

**Examples:**

The following are example uses for the vhdir-practitioner profile:

-  [George Washington MD, a cardiologist](Practitioner-practitioner1.html)


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each practitioner must have:

1.  A boolean value in `practitioner.active`
1.  One name in `practitioner.name`


**Profile specific implementation guidance:**

- TBD


**Extensions:**

1.  Endpoint (0..*) - reference(s) to the endpoint resource, indicating technical endpoints for the practitioner independent of their role at an organization
1.  Accessibility (0..*) - indicates accessibility options offered by the practitioner (e.g. cultural competence)
1.  Proficiency (0..1) - indicates a practitioner's level of spoken proficiency with the language(s) specified in `practitioner.communication`
1.  DigitalCertificate (0..*) - a digital certificate associated with the practitioner
1.  Qualification (0..1) - provides additional information about a practitioner's qualifications, including where they are valid and the current/historical status


**Terminology**

TBD