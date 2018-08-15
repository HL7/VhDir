---
title: Technical Guidance for VHDir Implementations
layout: default
active: technical-guidance
topofpage: true
sectionnumbering: true
F: http://build.fhir.org/

---

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->
**Contents**

* Do not remove this line (it will not be displayed)
{:toc}

---

<!-- end TOC -->

## Validated Healthcare Directory Concept Diagram

This diagram depicts the high-level conceptual design of a central source of validated healthcare directory data. 

<figure class="figure">
<figcaption class="figure-caption"><strong>Figure 1: Validated Healthcare Directory Concept Diagram</strong></figcaption>
  <img src="assets/images/conceptDiagram.jpg" class="figure-img img-responsive img-rounded center-block" alt="conceptDiagram.jpg" />
</figure>


In this diagram, RESTful FHIR APIs facilitate the movement data into and out of a validated healthcare directory (VHDir) at different points, including:
* Attestation: Individuals and organizations (via an authorized representative) attest to information about themselves for inclusion in the VHDir. See [link] for more information about attestation.
* Validation: An implementer of a VHDir (not shown in the diagram) may validate attested data against primary sources, thereby verifying the truthfulness and accuracy of the attested data. For example, an implementer might validate a provider’s medical license against records maintained by a state licensure board. Validation may occur initially, when attested data is first submitted, and/or on a regular basis as determined by the VHDir implementer and/or applicable laws, regulations, or policies. See [link] for more information about validation.
* Exchange: A VHDir would make validated healthcare directory data available to local workflow environments to support various business needs. Local workflow environments include, but are not limited to, payer organizations, provider organizations, health information exchanges (HIEs), health information service providers (HISPS), government agencies, and any other entities that maintain a healthcare directory and/or have a need for validated provider data. See [link] for more information about exchange.

## Attestation

Attestation describes the process by which authorized entities submit information about themselves, their roles, their relationships, etc. for inclusion in a healthcare directory. 

Guidance in this section is primarily intended to describe expectations for implementers using a FHIR API to manage attestation. An implementer’s unique implementation context, including local business needs, applicable laws/regulations/policies, usability considerations, etc. will determine an implementer’s approach to many of the attestation considerations described in this section. As we do not anticipate every implementer will use the same approach to attestation, we have not provided a set of attestation profiles or defined an attestation API. Implementers SHALL make any attestation requirements, including but not limited to profiles and/or API documentation, available to any stakeholders involved in the attestation process.

We acknowledge that implementers may use processes other than a FHIR API, such as paper-based forms, to obtain attested data. Such processes are considered out of scope for this guide.

This guide covers multiple attestation scenarios:
* Individual provider attesting to their information
* Authorized representative attesting to an individual provider’s information
* Authorized representative attesting to an organization’s information
* Authorized representative attesting to a payer organization’s information
* Submission of attested data by an authorized intermediary (e.g. another system that maintains attested data)

Each of these scenarios may encompass different sets of “permitted” data. For example, an individual provider attesting to her own information may not have the right to also attest to information about an organization she works for. These “rights” are assigned by each implementation of a validated healthcare directory, and can help prevent the submission of duplicate records. In general:
* An individual practitioner (or authorized representative) may attest to their own demographic information (e.g. name, birthdate, gender, etc.) and information about their relationships with organizations, locations, services, care teams, and health insurance provider networks.
  * Information represented using the Practitioner, PractitionerRole, Endpoint, and CareTeam profiles
* A provider organization (through an authorized representative) may attest to its own demographic information (e.g. name, address, contact info, etc.), services, locations, care teams and other organizations it owns/manages, and its relationships with other organizations, providers, and health insurance provider networks
  * Information represented using the Organization, PractitionerRole, OrganizationRole, HealthcareService, CareTeam, Location, and Endpoint profiles
  * In cases where individual practitioners operate as solo practitioners without a relationship to a legal organization, implementers should consider representing the individual using both a Practitioner and Organization resource and assigning the “organization” rights to the individual.
* A payer organization (through an authorized representative) may attest to its own demographic information (e.g. name, address, contact info, etc.), services, locations, care teams, other organizations, health insurance provider networks and products/plans it owns/manages, and its relationships with other organizations and providers.
  * Information represented as Organization, OrganizationRole, HealthcareService, CareTeam, Location, Endpoint, Network, and ProductPlan profiles
* An authorized intermediary may submit attested data on behalf of any of the previously described stakeholders. An intermediary should not submit data that has not been attested to, such as data that has been “scraped” from public sources. An example of an intermediary could be a state directory that collects information from providers in its jurisdiction, and then passes that information to a national directory.

Additionally, implementers may set requirements for the minimum amount of data different groups of stakeholders must attest to. For example, a US implementation might require all licensed providers to attest to their National Provider Identifier (NPI). In general, implementers might specify different minimum attestation requirements across three classes of stakeholders:
* Licensed billing providers (e.g. doctors, nurses)
* Non-licensed billing providers (e.g. medical equipment suppliers)
* Ancillary personnel (e.g. administrative staff)

We expect stakeholders will typically use a [SMART on FHIR application](https://smarthealthit.org/) to help attesters manage the attestation process (i.e. to submit attested data in the form of FHIR resources via a RESTful API). Such an application may be offered by an entity maintaining a validated healthcare directory or owned by the stakeholder(s) submitting attested data.

Before accepting attested data, a validated healthcare directory should have policies to ensure:
* Any attester application has successfully registered and integrated with the validated healthcare directory.
* Attesters have successfully completed any identify proofing requirements. 
* Any credentials or digital certificates that must be exchanged have been exchanged, validated, and are functional.
* The validated healthcare directory has set and made available any permissions/rights that govern the scope of data an attester may submit.
* Any representatives/intermediaries submitting data on behalf of an individual/entity have been appropriately authorized.

Once these preconditions have been met, a typical attestation workflow might involve:
* An attester application is pre-populated with data about the individual making the attestation, such as any known demographic information.
  * For example, the attester application may be pre-populated with data from the attester’s EHR system.
  * The attester application may query the validated healthcare directory for existing resources about the attester, which can be updated or used to pre-populate data in the application
* The application user enters the appropriate information and submits their attestation.
  * Submission of attested information may require some form of digital signature
  * The attester application may perform a validation process to check the general structure, content, etc. of the submission
* The attester application POSTs or PUTs the submitted data as FHIR resources to the validated healthcare directory’s attestation API
* The validated healthcare directory performs a validation process to check the general structure, content, etc. of the submission (e.g. checking consistency w/data type, required elements are present, references to existing resources are correct, codes are from appropriate value set etc.)
  * If there are no errors, the validated healthcare directory system assigns an id to the posted resources and returns the appropriate HTTP status code as well as the url/id of each resource
  * If there are errors, validated healthcare directory system rejects the operation and returns the appropriate HTTP status code and an OperationOutcome resource describing the error(s)

The FHIR specification [describes multiple approaches](http://build.fhir.org/http.html) for managing interactions over an API, including:
* Resources may be created, updated, patched, or deleted individually using the appropriate HTTP method (i.e. POST, PUT, PATCH, DELETE)
* Resources may be created, updated, patched, or deleted as a collection using a Bundle. A Bundle can include a set of actions to perform on a server in a single HTTP request/response.
  * A Bundle of type “batch” requires that there “SHALL be no interdependencies between the different entries in the Bundle,” but failure of any one interaction does not cause the whole collection to fail.
  * A Bundle of type “transaction” is processed as a single atomic unit, and the whole collection will fail if any of the interactions defined in the Bundle fail.
Additionally, the FHIR specification provides support for [asynchronous interactions](http://build.fhir.org/async.html), which may be necessary to facilitate processing of large amounts of data.

This implementation guide is not prescriptive about which approach(es) a validated healthcare directory should use to manage attestation. However, as any attestation will likely involve the submission of multiple FHIR resources representing information about one or more attesters, transaction Bundles can alleviate the need for more complex logic to manage referential integrity in attested information. 

Implementations relying on individual API interactions or batch Bundles may have to specify an “order of operations” to ensure attested data can be successfully submitted to the validated healthcare directory server. 

[insert proposed order of operations here]

Depending on the context of implementation, entities maintaining a validated healthcare directory may have to manage record collision or duplication (i.e. multiple attesters attempting to simultaneously submit updates to the same record, or multiple attesters attempting to attest about the same set of information).

The FHIR specification provides some [guidance](http://build.fhir.org/http.html#concurrency) on managing collisions using a combination of the ETag and If-Match header in an HTTP interaction. We recommend validated healthcare directory implementers use this approach.

To manage duplicate records, we generally recommend that validated healthcare directory implementers define a robust validation process with policies for identifying and resolving duplicates. Any additional technical capabilities are beyond the scope of this implementation guide.

## Validation

Validation is critical for ensuring that users of a healthcare directory can rely upon the data in the directory. Validation can refer to separate but related processes: validation of FHIR resources (e.g. checking consistency w/data type, required elements are present, references to existing resources are correct, codes are from appropriate value set etc.), and validation of data against a primary source (e.g. verifying an address using Post Office records). This section describes the latter.

Implementers will typically determine how primary source validation occurs operationally, based in part on the capabilities of the primary sources used for validation. For example, a primary source may already offer a mechanism like an API for validating content against its records. In other cases, an implementer may want to define an API that the primary source can access to push and/or pull content related to validation. Implementers may also consider less technical approaches, such as manual validation, or more stringent requirements, such as mailing a postcard to confirm an address. 

Certain types of data may have different validation requirements. For example, validating a relationship might require confirmation from each stakeholder participating in the relationship. Some data may have to be validated more frequently (e.g. license status), while other data can be validated once (e.g. education history) or not at all (e.g. a provider’s spoken language proficiency).

As with attestation, we expect VHDir implementers may use different approaches to validation. Therefore, we have not defined specific validation requirements or a validation API. Implementers SHALL make any validation requirements, including but not limited to profiles and/or API documentation, available to any stakeholders involved in the validation process.

This implementation guide includes a Validation profile for the VerificationResult resource for representing information about validation. The VerificationResult resource includes a number of data elements designed to record information pertaining to the validation processes defined by implementers, as well as the outcome of validation for a specific data element/set of elements/resource. The Validation profile includes data elements describing:
* The validation process, including the frequency of validation/revalidation, validation status, validation date, and what it means if validation was unsuccessful
* The primary source against which data was validated, including the identity of the primary source, how a validator communicates with the primary source, and whether the primary source can push updates about the data being validated
* The source of the data being validated (i.e. the attester), including the identity of the attesting individual, organization, and/or authorized representative and when the information was attested
* The entity conducting validation, including its identity and when it validated the data
* The outcome of validation for the targeted data

Validation may occur on the total contents of a resource, a collection of elements in a resource, or a single element. Any entity with access to a data element in a validated healthcare directory SHALL also have access to any validation information pertaining to that element. 

## Exchange

The primary focus of this implementation guide is a RESTful API for obtaining data from a Validated Healthcare Directory. The exchange API only supports a one-directional flow of information from a Validated Healthcare Directory into local environments (i.e. HTTP GETs). 

Conceptually, this guide was written to describe the flow of information from a central source of validated healthcare directory data to local workflow environments. We envisioned a national VHDir which functioned as a “source of truth” for a broad set of provider data available to support local business needs and use cases. A local environment could readily obtain all or a subset of the data it needed from the national VHDir and have confidence that the information was accurate. If necessary, a local environment could supplement VHDir data with additional data sourced and/or maintained locally. For example, a local environment doing provider credentialing might rely on a national VHDir for demographic information about a provider (e.g. name, address, educational history, license information, etc.), but also ask the provider for supplementary information such as their work history, liability insurance coverage, or military experience. Likewise, we envisioned that a VHDir would primarily share information with other systems, rather than individual end users or the general public. 

The content of this guide, however, does not preclude it from being implemented for smaller “local” directories, or accessed by the general public. Generally, conformance requirements throughout the guide are less tightly constrained so as to support a wider variety of possible implementations. We did not want to set strict requirements about the overall design, technical architecture, capabilities, etc. of a Validated Healthcare Directory that might prevent adoption of this standard. For example, although we would expect a national directory to gather and share information about healthcare provider insurance networks and health plans, implementations are not required to do so to be considered conformant (see the [Capability Statements Section](capstmnts.html) for more information about conformance).

We acknowledge that this decision has the potential to impact the interoperability of healthcare directory data and lead to variable implementations. However, we believe this risk is balanced by the potential for greater standardization of healthcare directory data enabled by this IG. We expect jurisdictions (e.g. countries) to further constrain this IG to meet their unique needs and publish the results openly and transparently.

Especially with larger-scale implementations, healthcare directories may contain a large amount of data that will not be relevant to all use cases or local needs. Therefore, the exchange API defines a number of search parameters to enable users to express the scope of a subset of data they care to access. For example, implementations are required to support searches for Organizations based on address, endpoint, identifier, name/alias, and relationship to a parent organization. In general, parameters for selecting resources based on a business identifier, status, type, or relationship (i.e. reference) are required for all implementations. Most parameters may be used in combination with other parameters and support more “advanced” capabilities like modifiers and chains.

The VHDir API currently supports one method for accessing directory data, a real-time pull. However, stakeholders may need other capabilities to support different business needs. For instance, stakeholders may need access to large amounts of VHDir data in a single session to either initially seed or refresh their local data repositories. Depending on the scope of data a stakeholder is trying to access, a real-time pull may not be the most effective method for acquiring large data sets. The FHIR specification provides support for [asynchronous interactions](http://build.fhir.org/async.html), which may be necessary for implementations to facilitate processing of large amounts of data.

VHDir implementations should also consider providing capabilities for users to subscribe to receive updates about the data they care about. A subscribe/publish model can help alleviate the need for stakeholders to periodically query a VHDir for new data and/or changes to data they have already obtained.

Likewise, implementers should consider supporting a mechanism to push urgent updates or changes to data that may impact business decisions or safety. For example, a VHDir might push updates about a practitioner’s record if their medical license is suspended or revoked.

## Restricted Content

We envisioned VHDir as a public or semi-public utility. Stakeholders who agreed to abide by the VHDir’s policies and procedures, signed a data use agreement, etc. would generally have access to VHDir data (Note: we consider specific operational policies and legal agreements out of scope for this IG). However, in some implementations, a VHDir may include sensitive data that is not publicly accessible or accessible to every VHDir stakeholder. For example, an implementer might not want to make data about military personnel, emergency responders/volunteers, or domestic violence shelters available to everyone with access to a VHDir, or to users in a local environment who have access to data obtained from a VHDir.

We expect that a VHDir’s operational policies and legal agreements will clearly delineate which data stakeholders can access, and if necessary, require stakeholders to protect the privacy/confidentiality of sensitive information in downstream local environments. As such, we have included a Restriction profile based on the Consent resource to convey any restrictions associated with a data element, collection of elements, or resource obtained from a VHDir.

## Must Support
*Must Support* on any data element SHALL be interpreted as follows:


* Validated Healthcare Directory Responders SHALL be capable of including the data element as part of the query results as specified by the [Validated Healthcare Directory Capability Statement].
* Validated Healthcare Directory Requestors SHALL be capable of processing resource instances containing the data elements without generating an error and causing the application to fail. In other words Validated Healthcare Directory Requestors SHOULD be capable of displaying the data elements for human use or storing it for other purposes.
* In situations where information on a particular data element is not present and the reason for absence is unknown, Validated Healthcare Directory Responders SHALL NOT include the data elements in the resource instance returned as part of the query results.
* When querying Validated Healthcare Directory Responders, Validated Healthcare Directory Requestors SHALL interpret missing data elements within resource instances as data not present in the Validated Healthcare Directory Responder's systems.
* In situations where information on a particular data element is missing and the Validated Healthcare Directory Responder knows the precise reason for the absence of data, Validated Healthcare Directory  Responders SHALL send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or using the dataAbsentReason extension.
* Validated Healthcare Directory Requestors SHALL be able to process resource instances containing data elements asserting missing information.


* NOTE: Typically *Validated Healthcare Directory Responder* Actor = Server and *Validated Healthcare Directory Requestor Actor* = Client
* NOTE: Validated Healthcare Directory Responders who do not have the capability to store or return a data element tagged as Supported in Validated Healthcare Directory profiles can still claim conformance to the Validated Healthcare Directory profiles per the Validated Healthcare Directory conformance resources.
* NOTE: The above definition of Supported is derived from HL7v2 concept "Required but may be empty - RE" described in HL7v2 V28_CH02B_Conformance.doc.
* NOTE: Readers are advised to understand [FHIR Terminology] requirements, [FHIR RESTful API] based on the HTTP protocol, along with [FHIR Data Types], [FHIR Search] and [FHIR Resource] formats before implementing Validated Healthcare Directory  requirements.


------------------------------------------------------------------------
