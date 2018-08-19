This profile sets minimum expectations for searching for and fetching information associated with a restriction. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the Consent resource when using this profile.

## Background and Context ##

The FHIR specification contains a security meta tag which can be used to inform systems of the sensitivity of resources. The tag can be used by access control mechanisms to ensure content isn't exposed inappropriately. However, the security meta tag can only indicate sensitivity at the resource level, and provides relatively little context about the restriction.

This implementation guide profiles the Consent resource to provide additional details about the nature of restrictions on content passed from the validated healthcare directory to downstream workflow environments. 

Typically, the "restriction" resource will function as a [contained resource](https://www.hl7.org/fhir/references.html#contained).

The restriction profile consists of the following elements:

*  `consent.status` indicates whether the restriction is active
*  `consent.category` describes the type of restriction (e.g. the data may be further disclosed by the downstream workflow environment per the terms of a Data Use Agreement)
*  `consent.dateTime` indicates when the restriction was last updated
*  `consent.policy` references a policy or policies defining the restriction
*  `consent.provision` defines access rights for restricted content


**Examples:**

The following are example uses for the vhdir-restriction profile:

-  [Restricted address for a women's shelter](Location-loc-ws.html)
-  [Restricted contact details for services provided by a women's shelter](HealthcareService-hcs-ws.html)


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each Consent resource must have:

1.  A coded value representing the status of the restriction in `consent.status`
1.  At least one coded and/or text value describing the type of restriction in `consent.category`
1.  At least one `actor` when describing access rights via `consent.provision`. Each actor must include a `reference` to a practitioner, organization, care team, or group. The `role` of each actor is fixed to code "IRCP" (information recipient) from the code system defined at <http://hl7.org/fhir/v3/ParticipationType>


**Profile specific implementation guidance:**

- TBD


**Terminology**

TBD