This profile sets minimum expectations for searching for and fetching information associated with a healthcare service. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the healthcareService resource when using this profile.

**Background & Scope**

The HealthcareService resource typically describes services offered by an organization at a location. The resource may be used to encompass a variety of services covering the entire healthcare spectrum, including promotion, prevention, diagnstics, hospital and ambulatory care, home care, long-term care, and other health-related and community services.

This profile adds optional extensions to describe whether a service is accepting new patients.

**Examples:**

The following are example uses for the vhdir-healthcareService profile:

-  [Cardiology Services](HealthcareService-ffcardiology.html)


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.   


1.  A boolean value in `healthcareService.active`


**Profile specific implementation guidance:**

- TBD


**Extensions:**

1.  NewPatients (0..*) - indicates whether the service is accepting new patients, consisting of:
    1.  AcceptingPatients (1.1) - a value of 'true' means the service is accepting new patients, 'false' means it is not
    1.  Network (0..1) - indicates whether the service is accepting new patients for a particular health provider insurance network
1.  NewPatientProfile (0..1) - a description of the type of patients the service accepts (e.g. pediatric only)


**Terminology**

TBD
