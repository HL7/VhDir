This profile sets minimum expectations for searching for and fetching information associated with a practitioner. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the Practitioner resource when using this profile.

**Background & Scope**

A practitioner is a person who is directly or indirectly involved in providing healthcare.

This profile modifies the base Practitioner resource in the following manner:

*  Constrains the cardinality of `practitioner.active` (1..1), `practitioner.name` (1..1), `practitioner.name.family` (1..1), `practitioner.name.given` (1..*), `practitioner.telecom.system` (1..1), `practitioner.telecom.value` (1..1), `practitioner.photo` (0..1), and `practitioner.qualification.issuer` (1..1)

*  All references SHALL conform to the appropriate Validated Healthcare Directory Implementation Guide profile

*  Adds extensions:

1.  [Identifier status](StructureDefinition-identifier-status.html) (1..1) - indicates the status of a practitioner's identifier
1.  [Via intermediary](StructureDefinition-contactpoint-viaintermediary.html) (0..1) - a reference to an alternative point of contact for this practitioner
1.  [Available time](StructureDefinition-contactpoint-availabletime.html) (0..*) - indicates when a practitioner is available for contact
1.  [Geolocation](http://hl7.org/fhir/StructureDefinition/geolocation) (0..1) - indicates the absolute geographic location of a practitioner's address
1.  [Endpoint](StructureDefinition-endpoint-reference.html) (0..*) - reference(s) to the endpoint resource, indicating technical endpoints for the practitioner independent of their role at an organization (such as a personal Direct address)
1.  [Accessibility](StructureDefinition-accessibility.html) (0..*) - indicates accessibility options offered by the practitioner (e.g. cultural competence)
1.  [Proficiency](StructureDefinition-communication-proficiency.html) (0..1) - indicates a practitioner's level of spoken proficiency with the language(s) specified in `practitioner.communication`
1.  [DigitalCertificate](StructureDefinition-digitalcertificate.html) (0..*) - a digital certificate associated with the practitioner
1.  [Qualification](StructureDefinition-practitioner-qualification.html) (0..1) - provides additional information about a practitioner's qualifications, including where they are valid and the current/historical status
1.  [Restriction](StructureDefinition-usage-restriction.html) (0..*) - indicates whether disclosure of any data associated with a practitioner is restricted

<!--- *  Adds new value sets/updates value set bindings:

TBD --->

**Examples:**

The following are example uses for the vhdir-practitioner profile:

-  [George Washington MD, a cardiologist](Practitioner-practitioner1.html)


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each practitioner must have:

1.  A boolean value in `practitioner.active`
1.  One name in `practitioner.name`
    1.  One family name in `practitioner.name.family`
    1.  At least one given name in `practitioner.name.given`


<!--- **Profile specific implementation guidance:**

- TBD --->