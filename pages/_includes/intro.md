
## {{ page.title }}

{% include publish-box.html %}

## Introduction

The Validated Healthcare Directory Implementation Guide is based on [FHIR Version 3.0.1](http://build.fhir.org/) and defines the minimum conformance requirements for accessing or exposing healthcare directory data.
Under the guidance of HL7 International, the Patient Administration workgroup, and the HL7 US Realm Steering Committee, the content intends to cover both international needs, along with a tightly bound set, tailored to meet the needs specific to the US Realm.

These requirements are being developed, in cooperation with the [Office of the National Coordinator for Health Information Technology (ONC)] and [Federal Health Architecture (FHA)](https://www.healthit.gov/policy-researchers-implementers/federal-health-architecture-fha) sponsored [Healthcare Directory Project] (HcDir) project. For more information on how DAF became Validated Healthcare Directory see the [Validated Healthcare Directory change notes](vhdir-change-notes.html).  

## Validated Healthcare Directory Actors

The following actors are part of the Validated Healthcare Directory IG:

* Validated Healthcare Directory Requestor: An application that initiates a data access request to retrieve patient data. This can be thought of as the client in a client-server interaction.
* Validated Healthcare Directory Responder: A product that responds to the data access request providing patient data. This can be thought of as the server in a client-server interaction.


## Validated Healthcare Directory Profiles

The list of Validated Healthcare Directory Profiles is shown below.  Each profile defines the minimum mandatory elements, extensions and terminology requirements that **MUST** be present. For each profile requirements and guidance are given in a simple narrative summary. A formal hierarchical table that presents a [logical view] of the content in both a differential and snapshot view is also provided along with references to appropriate terminologies and examples.  In addition each profile has a "Quick Start" section which is intended as an implementer friendly overview of the required search and read operations.

{% include list-simple-profiles.xhtml %}

*Note on Searches based on a date or date range:*

- Allergies, Immunizations, Medications, Problems and Health Concerns, UDI, Smoking Status do not require a date range search since a system should return all relevant resources.
- Vital Signs, Laboratory Results, Goals, Procedures, and Assessment and Plan of Treatment include date range search requirements in the Quick Start section on the profile page.

## Validated Healthcare Directory Conformance Requirements

The [Capability Statements Section](capstmnts.html) outlines conformance requirements for the Validated Healthcare Directory Servers and Client applications, identifying the specific profiles that need to be supported, the specific RESTful operations that need to be supported, and the search parameters that need to be supported. Note: The individual Validated Healthcare Directory profiles identify the structural constraints, terminology bindings and invariants, however, implementers must refer to the conformance requirements for details on the RESTful operations, specific profiles and the search parameters applicable to each of the Validated Healthcare Directory actors.

----

Primary Authors: Brian Postlethwaite, Bob Dieterle, ONC Contributors

Secondary Authors: Grahame Grieve, Lloyd McKenzie

[Argonaut]: http://argonautwiki.hl7.org/index.php?title=Main_Page
[Validated Healthcare Directory Security]: US Core-security.html
[Office of the National Coordinator for Health Information Technology (ONC)]: http://www.healthit.gov/newsroom/about-onc
[Data Access Framework]: http://wiki.siframework.org/Data+Access+Framework+Homepage
[profiles]: http://hl7.org/fhir/STU3/profiling.html
[logical view]: http://hl7.org/fhir/STU3/formats.html#table
[StructureDefinitions]: http://hl7.org/fhir/STU3/structuredefinition.html
[Value sets]: http://hl7.org/fhir/STU3/valueset.html
[CodeSystem]: http://hl7.org/fhir/STU3/codesystem.html
[ConceptMap]: http://hl7.org/fhir/STU3/conceptmap.html
[NamingSystem]: http://hl7.org/fhir/STU3/namingsystem.html
[FHIR Conformance Rules]: http://hl7.org/fhir/STU3/CapabilityStatement-rules.html
[dataAbsentReason]: http://hl7.org/fhir/STU3/extension-data-absent-reason.html
[FHIR Terminology]: http://hl7.org/fhir/STU3/terminologies.html
[FHIR RESTful API]: http://hl7.org/fhir/STU3/http.html
[HTTP]: http://hl7.org/fhir/STU3/http.html
[FHIR Data Types]: http://hl7.org/fhir/STU3/datatypes.html
[FHIR Search]: http://hl7.org/fhir/STU3/search.html
[FHIR Resource]: http://hl7.org/fhir/STU3/formats.html
[2015 Edition Common Clinical Data Set]: guidance.html#edition-common-clinical-data-set
