---
title: Terminology defined for the Validated Healthcare Directory Implementation Guide
layout: default
active: terminology
topofpage: true
sectionnumbering: true
F: http://build.fhir.org/
---

This page lists all the ValueSets, CodeSystems, and ConceptMaps defined as part of the Validated Healthcare Directory implementation Guide. For more information on using codes in resources, see the [guidance section](guidance.html#using-codes-in-vhdir-profiles) as well as in the [FHIR specification](http://hl7.org/fhir/STU3/terminologies.html).

All code systems and value sets in the guide are proposed and undergoing review and harmonization.

#### Value Sets

{% include list-simple-valuesets.xhtml %}

<p/><p/>

<!--

These list cross references codes and codable concepts proposed for this implementation guide mappign them to the resources and data elements where they are used.

|Element|Type|Proposed values/Comments|
|---|---|---|
digitalCertificate.type|code|TLS/SSL; device; identity; group
digitalCertificate.use|code|digsig; keyEncipherment
digitalCertificate.certificateStandard|code|x.509v3
digitalCertificate.trustFramework|CodeableConcept|DirectTrust; FBCA; other
accessibility.type (on pracitioner & location)|CodeableConcept|Cultural competence; handicap accessible; ADA compliant; public transit options; answering service
practitioner.communication.proficiency|CodeableConcept|Use ILR scale: 0 (no proficiency); 1 (elementary proficiency); 2 (limited working proficiency); 3 (professional working proficiency); 4 (full professional proficiency)
organization.alias.type|code|DBA; historical; other
organizationrole.role|CodeableConcept|provider; agency; research; payer; diagnostics; supplier; HIE/HIO; member - Note: There are a number of potential value sets to use, one specific to this IG may be created
organizationRole.specialty|CodeableConcept|Value set may be based on qualified clinical specialty codes from NUCC
ehr.certificationEdition|CodeableConcept|2011; 2014; 2015
ehr.patientAccess|CodeableConcept|patient portal; secure messaging; view/download/transmit (VDT)
careteam.mode|code|instance; kind
endpoint.useCase.type|CodeableConcept|An enumeration of specific use cases (service descriptions) supported by the endpoint
VerificationResult.validationNeed|code|none; initial; periodic
VerificationResult.validationStatus|code|attested; validated; in process; requires revalidation; validation failed; revalidation failed
VerificationResult.validationType|code|nothing; primary source; multiple sources
VerificationResult.validationProcess|code|edit check; value set; primary source; multiple sources; standalone; in context
VerificationResult.failureAction|code|fatal; warning; record only; none
VerificationResult.primarySource.sourceType|CodeableConcept|License Board; Primary Education; Continuing Education; Postal Service; Relationship owner; Registration Authority; legal source; issuing source; aughorative source
VerificationResult.primarySource.validationProcess|code|manual; API; push
VerificationResult.primarySource.validationStatus|code|successful; failed; undetermined
VerificationResult.primarySource.CanPushUpdates|code|yes; no; undetermined
VerificationResult.primarySource.PushTypeAvailable|code|specific requested changes; any changes; as defined by source
VerificationResult.attestation.attestationMethod|code|(owner; authorized representative; authorized intermediary; non-authorized source)
network.type|Coding|PPO; HMO; ACO; Speciality; Dental; Vision; Pharmacy; National; Regional; State
productPlan.type|Coding|Medical; Dental; Mental Health; Substance Abuse; Vision; Drug; Short Term. Long Term Care, Hospice, Home Health
productCoverage.benefits.benefitsList.description|CodeableConcept|Days; visits
plan.planType|CodeableConcept|Platinum; Gold; Silver; Bronze; High Deductable; Low Deductable
plan.benefitCategory.benefitType.type|CodeableConcept|preventative , primary care office visit, speciality office visit, hospitalization; emergency room; urgent care
restriction.type|CodeableConcept|conditional release (per DUA); requires flowdown agreement (for redisclosure); internal use only; release defined by access rights (as specified by the national resource)
restriction.reason.reasonType|code|contributes to; reason for; existance of; specific value
restriction.accessRights|Reference|This value set is proposed, additional review required - http://hl7.org/fhir/valueset-security-labels.html
restriction.identifer.status|code|active; inactive; issued in error; revoked; pending

-->

#### Code Systems

See the [FHIR terminology section](http://hl7.org/fhir/STU3/terminologies-systems.html) for a complete discussion on code systems and a list of codes system names used in FHIR. The following additional names (URIs) have been identified for this implementation guide,   If a URI is listed here, it **SHALL** be used in the Validated Healthcare Directory profiles in preference to any other code system name.

**Code systems published in this IG** - Includes Validated Healthcare Directory defined code systems and externally defined code systems

{% include list-simple-codesystems.xhtml %}

<p/><p/>

**Internally Published code systems - FHIR**

|URI|Source|Comment|OID (for OID based Terminolgy Systems)|Used in
|---|---|---|---|
|http://hl7.org/fhir/administrative-gender|[FHIR](https://www.hl7.org/fhir/valueset-administrative-gender.html)|*Administrative Gender*|2.16.840.1.113883.4.642.3.1|Pracitioner.gender
|https://www.hl7.org/fhir/v2/0360/2.7/index.html|[FHIR (HL7V2)](http://hl7.org/fhir/v2/0360/2.7)|*Listed as a V2 data set, but there is a FHIR copy also*|None listed|Qualification.code
|http://hl7.org/fhir/valueset-organization-type.html|[FHIR](http://hl7.org/fhir/valueset-organization-type.html)|*The type of the organization - this list from FHIR will need to be extended*|	2.16.840.1.113883.4.642.3.403|Organization.type
|http://hl7.org/fhir/valueset-practitioner-role.html|[FHIR](http://hl7.org/fhir/valueset-practitioner-role.html)|*Defines a set of codes that can be used to indicate the role of a Practitioner or Organization - Assume this will extended to organizational roles*|2.16.840.1.113883.4.642.3.430|PracitionerRole.code; OrganizationRole.Code
|http://hl7.org/fhir/codesystem-practitioner-specialty.html|[FHIR](http://hl7.org/fhir/codesystem-practitioner-specialty.html)|*Defines a set of codes that can be used to indicate the specialty of a Practitioner or Organization. Assume this will be extended to include Organization Roles*|2.16.840.1.113883.4.642.1.433|PracitionerRole.speciality; OrganizationRole.specialty
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
|http://hl7.org/fhir/ValueSet/care-team-category|[FHIR](http://hl7.org/fhir/codesystem-care-team-category.html)|*Indicates the type of care team*|2.16.840.1.113883.4.642.1.147|CareTeam.category
|http://hl7.org/fhir/ValueSet/participant-role|[FHIR](http://hl7.org/fhir/ValueSet/participant-role)|*Roles of Participants that may be included in a CarePlan.Participants, or in an EpisodeOfCare.CareTeam. Defined as: Is a Person, Healthcare professional (occupation) or Healthcare related organization (qualifier value).*|	2.16.840.1.113883.4.642.3.143|CareTeam.participant.role
|http://hl7.org/fhir/ValueSet/clinical-findings|[FHIR](http://hl7.org/fhir/ValueSet/clinical-findings)|*This value set includes all the "Clinical finding"*|2.16.840.1.113883.4.642.3.227|CareTeam.reasonCode
|http://hl7.org/fhir/ValueSet/endpoint-status|[FHIR](https://www.hl7.org/fhir/codesystem-endpoint-status.html)|*The status of the endpoint*|2.16.840.1.113883.4.642.1.488|Endpoint.status
|http://hl7.org/fhir/ValueSet/endpoint-connection-type|[FHIR](http://hl7.org/fhir/codesystem-endpoint-connection-type.html)|*Represents possible connection type profile values*|2.16.840.1.113883.4.642.3.491|Endpoint.connectionType
|http://hl7.org/fhir/ValueSet/endpoint-payload-type|[FHIR](http://hl7.org/fhir/codesystem-endpoint-payload-type.html)|*Represents possible payload document types*|2.16.840.1.113883.4.642.3.489|Endpoint.payloadType
http://hl7.org/fhir/name-use|[FHIR](http://hl7.org/fhir/name-use)|*The use of a human name*|2.16.840.1.113883.4.642.3.58|HumanName.use
http://hl7.org/fhir/contact-point-system|[FHIR](http://hl7.org/fhir/contact-point-system)|*Telecommunications form for contact point*|2.16.840.1.113883.4.642.3.64|ContactPoint.system
http://hl7.org/fhir/contact-point-use|[FHIR](http://hl7.org/fhir/contact-point-use)|*Use of contact point*|2.16.840.1.113883.4.642.3.64|ContactPoint.use
http://hl7.org/fhir/days-of-week|[FHIR](http://hl7.org/fhir/days-of-week)|*This value set is the designated 'entire code system' value set for DaysOfWeek*|2.16.840.1.113883.4.642.3.506 |ContactPoint.Availabletime.DaysOfWeek
http://hl7.org/fhir/address-use|[FHIR](http://hl7.org/fhir/address-use)|*The use of an address*|2.16.840.1.113883.4.642.3.60|Address.Use
http://hl7.org/fhir/address-type|[FHIR](http://hl7.org/fhir/address-type)|*The type of an address (physical / postal)*|2.16.840.1.113883.4.642.3.62|Address.Type
http://hl7.org/fhir/identifier-use|[FHIR](http://hl7.org/fhir/identifier-use)|*Identifies the purpose for this identifier, if known .*|2.16.840.1.113883.4.642.3.52|Identifier.Use
http://hl7.org/fhir/identifier-type|[FHIR](http://hl7.org/fhir/identifier-type)|*A coded type for an identifier that can be used to determine which identifier to use for a specific purpose.*|2.16.840.1.113883.4.642.3.44|Identifier.Type

#### Externally Published code systems *

|URI|Source|Comment|OID (for non-FHIR systems)
|---|---|---|---|
|http://nucc.org/provider-taxonomy|[NUCC](http://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40/csv-mainmenu-57)|*NUCC Provider Taxonomy*|2.16.840.1.113883.6.101|Proposed for organizationRole above
|http://www.rfc-editor.org/bcp/bcp13.txt|http://www.rfc-editor.org/bcp/bcp13.txt|*Defininitions for mimeType|TBD|Endpoint.payloadMimeType

<p/><p/>

#### ConceptMaps defined as part of the Validated Healthcare Directory Implementation Guide

{% include list-simple-conceptmaps.xhtml %}
