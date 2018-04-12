## Validated Healthcare Directory Conformance Requirements
{:.no_toc}

This section outlines conformance requirements for the Validated Healthcare Directory and Client applications, identifying the specific profiles that need to be supported, the specific RESTful operations that need to be supported, and the search parameters that need to be supported. 

---

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->
**Contents**

* Do not remove this line (it will not be displayed)
{:toc}

---

<!-- end TOC -->


### Conformance requirements for the Validated Healthcare Directory

Source Resource: [XML](CapabilityStatement-server.xml.html)/[JSON](CapabilityStatement-server.json.html)

1. FHIR Version: 4.0
1. Supported formats: xml, json
1. Published: Draft
1. Published by: Health Level Seven International the Patient Administration Workgroup and the HL7 US Realm Steering Committee.

This section describes the expected capabilities of the Validated Healthcare Directory actor that is responsible for providing responses to the queries submitted by the Validated Healthcare Directory Requestors. The complete list of FHIR profiles, RESTful operations, and search parameters supported by Validated Healthcare Directory are defined. 

#### Behavior

Description:

The Validated Healthcare Directory responder **SHALL**: 

1. Support the Validated Healthcare Directory resource profiles.
1. Implement the RESTful behavior according to the FHIR specification.
1. Return the following response classes:
   - (Status 200): successful operation
   - (Status 400): invalid parameter
   - (Status 401/4xx): unauthorized request
   - (Status 403): insufficient scope
   - (Status 404): unknown resource
   - (Status 410): deleted resource.
1. Support *json* resource formats for all Validated Healthcare Directory interactions.
1. Declare a CapabilityStatement identifying the list of profiles, operations, search parameter supported.

The Validated Healthcare Directory responder **SHOULD**:

1. Support *xml* resource formats for all Validated Healthcare Directory interactions.
1. Identify the Validated Healthcare Directory profiles supported as part of the FHIR `meta.profile` attribute for each instance.

#### Security:

The Validated Healthcare Directorys responder **SHALL**:

1. Implement the [security requirements](security.html) documented in the this IG.
1. A server has ensured that every API request includes a valid Authorization token, supplied via: `Authorization: Bearer {server-specific-token-here}`
1. A server has rejected any unauthorized requests by returning an `HTTP 401` Unauthorized response code.

#### Profile Interaction Summary:

1. All servers **SHALL** make available the [read](http://hl7.org/fhir/STU3/http.html#read) and [search](http://hl7.org/fhir/STU3/http.html#search) interactions for all the Profiles.
1. All servers **SHOULD** make available the [vread](http://hl7.org/fhir/STU3/http.html#vread) and [history-instance](http://hl7.org/fhir/STU3/http.html#history) interactions for all the Profiles.

#### Summary of Validated Healthcare Directory search criteria:

Specific server search capabilities are under analysis. 

#### Resource  Details:

{:.no_toc}

Supported Profiles:  Specific profile support requirements are under analysis.

<p></p>
