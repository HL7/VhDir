
## Terminology defined for the Validated Healthcare Directory Implementation Guide

This page lists all the ValueSets, CodeSystems, and ConceptMaps defined as part of the Validated Healthcare Directory implementation Guide. For more information on using codes in resources, see the [guidance section](guidance.html#using-codes-in-vhdir-profiles) as well as in the [FHIR specification](http://hl7.org/fhir/STU3/terminologies.html).

#### Value Sets

These value sets have been defined for this implementation guide.

{!% include list-simple-valuesets.xhtml %!}

#### Code Systems

See the [FHIR terminology section](http://hl7.org/fhir/STU3/terminologies-systems.html) for a complete discussion on code systems and a list of codes system names used in FHIR. The following additional names (URIs) have been identified for this implementation guide,   If a URI is listed here, it **SHALL** be used in the US Core profiles in preference to any other code system name.

**Code systems published in this IG** - Includes US Core defined code systems and externally defined code systems

<!-- {sdf% include list-simple-codesystems.xhtml %} -->

|URI|Source|Comment|OID (for OID based Terminolgy Systems)|Used in
|---|---|---|---|
|TBD|TBD|*Type for digital certificate (encryption (SSL); encryption (other); device; identity; signing; group; Direct messaging encryption (SSL)*|TBD|digitalCertificate.type
|TBD|TBD|*Standard for digital certificate - only known value is x.509v3*|TBD|digitalCertificate.certificateStandard
|TBD|TBD|*Trust Framework - (DirectTrust; FBCA; others?)*|TBD|digitalCertificate.trustFramework
|TBD|TBD|*Accessibility Type (Cultural Competancy; handicap accessible; ADA compliant; public transit options; answering service; etc.)*|TBD|Practitioner.accessability.type
|TBD|TBD|*A type the describes the type of alias (DBA; Historical; Other)*|TBD|alias.type
|TBD|TBD|*Describes a profile for new patients, e.g. less than a certain age, of a particular gender, etc; a combination of codes; free form text if no options meet the need*|TBD|PrectitionerRole.newPatientProfile
|TBD|TBD|*The code(s) that detail specific eligability requirements for using/obtaining this service*|TBD|HealthcareService.eligibility
|TBD|TBD|*The code(s) that describe a collection of characteristics about the service*||HealthcareService.characteristic
|TBD|TBD|*The code(s) that detail the ways this servce accepts referrals*||HealthcareService.referralMethod
|TBD|TBD|*Indicates the version of certifcation of the Health IT Module(s) at this location*|TBD|Location.certificationEdition
|TBD|TBD|*Indicates any patient access to Health IT products at this location e.g. patient portal, download C-CDA, etc.*|TBD|Location.patientAccess
TBD|TBD|*validation need (none; initial; periodic)*|TBD|validation.validationNeed
TBD|TBD|*status of the element or related elements (attested; validated; in process; requires revalidation; validation failed; revalidation failed)*|TBD|validation.validationStatus
TBD|TBD|*what is this validated against (nothing; primary source; multiple sources)*|TBD|validation.validationType
TBD|TBD|*Process(es) (primary) (edit check, value set. primary source, multiple sources, standalon, in context)*|TBD|validation.validationProcess
TBD|TBD|*Frequency of revalidation (need reasonable frequency list) *|TBD|validation.frequency
TBD|TBD|*if validation failed (fatal; warning; record only; none)*|TBD|validation.failureAction
TBD|TBD|*reference source for element validation*|TBD|validation.primarysources.source
TBD|TBD|*Type for each source (dynamic value set -- need initial list)*|TBD|validation.primarysources.sourceType
TBD|TBD|*Process(es) (manual, API, Push)*|TBD|validation.primarysources.sourceValidationProcess
TBD|TBD|*success or failure on last validation*|TBD|validation.primarysources.sourceValidationStatus
TBD|TBD|*source ability to alert (push updates) (Yes, No)*|TBD|validation.primarysources,sourcePush
TBD|TBD|*type of alert(s) (need code list)*|TBD|validation.primarysources.sourcepushtype
TBD|TBD|*tbd*|TBD|validation.attestation.attestationMethod

<p>
</p>

**Internally Published code systems - FHIR**

|URI|Source|Comment|OID (for OID based Terminolgy Systems)|Used in
|---|---|---|---|
|`http://hl7.org/fhir/administrative-gender`|[FHIR](https://www.hl7.org/fhir/valueset-administrative-gender.html)|*Administrative Gender*|2.16.840.1.113883.4.642.3.1|Pracitioner.gender
|`https://www.hl7.org/fhir/v2/0360/2.7/index.html`|[FHIR (HL7V2)](http://hl7.org/fhir/v2/0360/2.7)|*Listed as a V2 data set, but there is a FHIR copy also*|None listed|Qualification.code
|TBD|TBD|*proficiency - level of proficiency for language spoken based on ILR scale, CEFR, or ACTFL*|TBD|Practitioner.languageSpoken.proficiency
|http://hl7.org/fhir/valueset-organization-type.html|[FHIR](http://hl7.org/fhir/valueset-organization-type.html)|*The type of the organization - this list from FHIR will need to be extended*|	2.16.840.1.113883.4.642.3.403|Organization.type
|http://hl7.org/fhir/valueset-practitioner-role.html|[FHIR](http://hl7.org/fhir/valueset-practitioner-role.html)|*Defines a set of codes that can be used to indicate the role of a Practitioner or Organization - Assume this will extended to organizational roles*|2.16.840.1.113883.4.642.3.430|PracitionerRole.code; OrganizationRole.Code
|http://hl7.org/fhir/codesystem-practitioner-specialty.html|[FHIR](http://hl7.org/fhir/codesystem-practitioner-specialty.html)|*Defines a set of codes that can be used to indicate the specialty of a Practitioner or Organization. Assume this will be extended to include Organization Roles*|2.16.840.1.113883.4.642.1.433|PracitionerRole.speciality; OrganizationRole.specialty
|TBD|[TBD]|*Defines a set of codes that can be used to indicate the subspecialty of a Practitioner.*|TBD|PracitionerRole.speciality.subspecialty
|https://www.hl7.org/fhir/valueset-service-category.html|[FHIR](https://www.hl7.org/fhir/codesystem-service-category.html)|*This value set defines an example set of codes that can be used to classify groupings of service-types/specialties*|	2.16.840.1.113883.4.642.3.511|HealthcareService.category
|https://www.hl7.org/fhir/valueset-service-type.html|[FHIR](https://www.hl7.org/fhir/valueset-service-type.html)|*This value set defines an example set of codes of service-types*|	2.16.840.1.113883.4.642.3.512|HealthcareService.type
|https://www.hl7.org/fhir/valueset-c80-practice-codes.html|[FHIR](https://www.hl7.org/fhir/valueset-c80-practice-codes.html)|*This is the code representing the clinical specialty of the clinician or provider who interacted with, treated, or provided a service to/for the patient. The value set used for clinical specialty has been limited by HITSP to the value set reproduced from HITSP C80 Table 2-149 Clinical Specialty Value Set Definition.*|2.16.840.1.113883.3.88.12.80.72|HealthcareService.specialty
|http://hl7.org/fhir/valueset-service-provision-conditions.html|[FHIR](http://hl7.org/fhir/valueset-service-provision-conditions.html)|The code(s) that detail the conditions under which the healthcare service is available/offered|2.16.840.1.113883.4.642.3.508|HealthcareService.serviceProvisionCode
|http://hl7.org/fhir/codesystem-days-of-week.html|[FHIR](http://hl7.org/fhir/codesystem-days-of-week.html)|*The days of the week.*|2.16.840.1.113883.4.642.1.507|PractitionerRole.availableTime.daysOfWeek; OrganizationRole.availableTime.daysOfWeek; HealthcareService.daysOfWeek
|https://www.hl7.org/fhir/codesystem-location-status.html|[FHIR](https://www.hl7.org/fhir/codesystem-location-status.html)|*Indicates whether the location is still in use. (active; suspended; inactive)*|2.16.840.1.113883.4.642.1.324|Location.status
|http://hl7.org/fhir/ValueSet/location-mode|[FHIR](http://hl7.org/fhir/valueset-location-mode.html)|*Indicates whether a resource instance represents a specific location or a class of locations (instance; kind)*|2.16.840.1.113883.4.642.3.321|Location.mode
|http://hl7.org/fhir/ValueSet/v3-ServiceDeliveryLocationRoleType|[FHIR](http://hl7.org/fhir/v3/RoleCode/cs.html)|*A role of a place that further classifies the setting (e.g., accident site, road side, work site, community location) in which services are delivered.*|2.16.840.1.113883.5.111|Location.type
|http://hl7.org/fhir/ValueSet/location-physical-type|[FHIR](https://www.hl7.org/fhir/codesystem-location-physical-type.html)|*This example value set defines a set of codes that can be used to indicate the physical form of the Location*|2.16.840.1.113883.4.642.1.320|Location.physicalType
|http://hl7.org/fhir/ValueSet/care-team-status|[FHIR](https://www.hl7.org/fhir/codesystem-care-team-status.html)|*Indicates the status of the care team*|2.16.840.1.113883.4.642.1.145|CareTeam.status
|http://hl7.org/fhir/ValueSet/care-team-category|[FHIR](http://hl7.org/fhir/codesystem-care-team-category.html)||*Indicates the tyoe of care team*|2.16.840.1.113883.4.642.1.147|CareTeam.category
|http://hl7.org/fhir/ValueSet/participant-role|[FHIR](http://hl7.org/fhir/ValueSet/participant-role)|*Roles of Participants that may be included in a CarePlan.Participants, or in an EpisodeOfCare.CareTeam. Defined as: Is a Person, Healthcare professional (occupation) or Healthcare related organization (qualifier value).*|	2.16.840.1.113883.4.642.3.143|CareTeam.participant.role
|http://hl7.org/fhir/ValueSet/clinical-findings|[FHIR](http://hl7.org/fhir/ValueSet/clinical-findings)|*This value set includes all the "Clinical finding"*|2.16.840.1.113883.4.642.3.227|CareTeam.reasonCode
|http://hl7.org/fhir/ValueSet/endpoint-status|[FHIR](https://www.hl7.org/fhir/codesystem-endpoint-status.html)|*The status of the endpoint*|2.16.840.1.113883.4.642.1.488|Endpoint.status
|http://hl7.org/fhir/ValueSet/endpoint-connection-type|[FHIR](http://hl7.org/fhir/codesystem-endpoint-connection-type.html)|*Represents possible connection type profile values*|2.16.840.1.113883.4.642.3.491|Endpoint.connectionType
|http://hl7.org/fhir/ValueSet/endpoint-payload-type|[FHIR](http://hl7.org/fhir/codesystem-endpoint-payload-type.html)|*Represents possible payload document types*|2.16.840.1.113883.4.642.3.489|Endpoint.payloadType
http://hl7.org/fhir/name-use|FHIR|*The use of a human name*|2.16.840.1.113883.4.642.3.58|HumanName.use
http://hl7.org/fhir/contact-point-system|FHIR|*Telecommunications form for contact point*|2.16.840.1.113883.4.642.3.64|ContactPoint.system
http://hl7.org/fhir/contact-point-use|FHIR|*Use of contact point*|2.16.840.1.113883.4.642.3.64|ContaPoint.use
http://hl7.org/fhir/days-of-week|FHIR|*This value set is the designated 'entire code system' value set for DaysOfWeek*|2.16.840.1.113883.4.642.3.506 |ContactPoint.Availabletime.DaysOfWeek
http://hl7.org/fhir/address-use|FHIR|*The use of an address*|2.16.840.1.113883.4.642.3.60|Address.Use
http://hl7.org/fhir/address-type|FHIR|*The type of an address (physical / postal)*|2.16.840.1.113883.4.642.3.62|Address.Type
http://hl7.org/fhir/identifier-use|FHIR|*Identifies the purpose for this identifier, if known .*|2.16.840.1.113883.4.642.3.52|Identifier.Use
http://hl7.org/fhir/identifier-type|FHIR|*A coded type for an identifier that can be used to determine which identifier to use for a specific purpose.*|2.16.840.1.113883.4.642.3.44|Identifier.Type
hl7.org/fhir/vhdir/identifier-status |TBD|*Status of the ID*|TBD|Identifier.Status
hl7.org/fhir/vhdir/restriction-restrictionType |TBD|*what is the restriction (reference to DUA standard item)*|TBD|Restriction.restrictionType
hl7.org/fhir/vhdir/restriction-retrospective|TBD|*is the restriction retrospective (yes, no)*|TBD|Restriction.retrospective
hl7.org/fhir/vhdir/restriction-reason-reasonType|TBD|*Code*|TBD|Restriction.reaston.reasonType

**Internally Published code systems - HL7 V3**

*None*

**Internally Published code systems HL7 V2**

*None*

**Externally Published code systems **

|URI|Source|Comment|OID (for non-FHIR systems)
|---|---|---|---|
|`http://nucc.org/provider-taxonomy`|[NUCC](http://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40/csv-mainmenu-57)|*NUCC Provider Taxonomy*|2.16.840.1.113883.6.101
|http://www.rfc-editor.org/bcp/bcp13.txt|http://www.rfc-editor.org/bcp/bcp13.txt|*Defininitions for mimeType|TBD|Endpoint.payloadMimeType


<!--
|[urn:oid:2.16.840.1.113883.6.238](CodeSystem-cdcrec.html)|[CDC](https://www.cdc.gov/phin/resources/vocabulary/index.html)|*Race & Ethnicity - CDC* - See [CDC Race and Ethnicity Code Set Version 1.0](https://www.cdc.gov/phin/resources/vocabulary/documents/cdc-race--ethnicity-background-and-purpose.pdf).|2.16.840.1.113883.6.238
-->

<p>
</p>

#### ConceptMaps

The following concept mappings have been defined as part of the this guide.

  <!-- {sdf% include list-simple-conceptmaps.xhtml %} -->
<p>
</p>
