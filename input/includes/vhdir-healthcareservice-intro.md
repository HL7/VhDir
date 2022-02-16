This profile sets minimum expectations for searching for and fetching information associated with a healthcare service. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the HealthcareService resource when using this profile.

**Background & Scope**

The HealthcareService resource typically describes services offered by an organization/practitioner at a location. The resource may be used to encompass a variety of services covering the entire healthcare spectrum, including promotion, prevention, diagnstics, hospital and ambulatory care, home care, long-term care, and other health-related and community services.

This profile modifies the base HealthcareService resource in the following manner:

*  Constrains the cardinality of `healthcareService.active` (1..1), `healthcareService.telecom.system` (1..1), and `healthcareService.telecom.value` (1..1)

*  All references SHALL conform to the appropriate Validated Healthcare Directory Implementation Guide profile

*  Adds extensions:

1.  [Identifier status](StructureDefinition-identifier-status.html) (1..1) - indicates the status of a service's identifier
1.  [Via intermediary](StructureDefinition-contactpoint-viaintermediary.html) (0..1) - a reference to an alternative point of contact for this service
1.  [Available time](StructureDefinition-contactpoint-availabletime.html) (0..*) - indicates when a service is available for contact
1.  [NewPatients](StructureDefinition-newpatients.html) (0..*) - indicates whether the service is accepting new patients
1.  [Restriction](StructureDefinition-usage-restriction.html) (0..*) - indicates whether disclosure of any data associated with a service is restricted



**Examples:**

The following are example uses for the vhdir-healthcareservice profile:

-  [Cardiology Services](HealthcareService-ffcardiology.html)


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.   


1.  A boolean value in `healthcareService.active`

<!--
**Profile specific implementation guidance:**

- TBD -->
