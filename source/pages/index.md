---
title: Validated Healthcare Directory Implementation Guide HomePage
layout: default
active: home
topofpage: true
sectionnumbering: true
F: http://build.fhir.org/
---

{% include publish-box.html %}

## Introduction

The Validated Healthcare Directory Implementation Guide (VHDir IG) is based on [FHIR Version 4.0](http://build.fhir.org/). It was developed in cooperation with the [Office of the National Coordinator for Health Information Technology (ONC)](http://www.healthit.gov/newsroom/about-onc) and [Federal Health Architecture (FHA)](https://www.healthit.gov/policy-researchers-implementers/federal-health-architecture-fha) with guidance from HL7 International, the Patient Administration Workgroup, and the HL7 US Realm Steering Committee.

It describes the architectural considerations for attesting to, validating, and exchanging data from a central source of validated provider data (i.e. a Validated Healthcare Directory or VHDir), as well as a RESTful FHIR API for accessing data from a VHDir.

Although we developed this guide from the conceptual starting point of a national source of validated provider data, we recognize that implementers may have different business needs, contexts, or use cases. Therefore, we have strived to make this guide as broadly applicable as possible. Every implementation may not use all of the content in this guide. It serves as a “floor” for the exchange of validated provider data, while describing additional data elements and capabilities that support more robust implementations. 

Likewise, we provide general guidance about the technical architecture and capabilities of a central source of validated provider data, but are not prescriptive about what an implementation must include.  

For more information on the history of Validated Healthcare Directory see the [Validated Healthcare Directory change notes](vhdir-change-notes.html).


## Validated Healthcare Directory Profiles

The list of Validated Healthcare Directory Profiles is shown below.  Each profile defines the minimum mandatory elements, extensions and terminology requirements that **MUST** be present. For each profile, requirements and guidance are given in a simple narrative summary. A formal hierarchical table that presents a [logical view] of the content in both a differential and snapshot view is also provided along with references to appropriate terminologies and examples.  In addition each profile has a "Quick Start" section which is intended as an implementer friendly overview of the required search and read operations.

{% include list-simple-profiles.xhtml %}


## Validated Healthcare Directory Conformance Requirements

The [Capability Statements Section](capstmnts.html) outlines conformance requirements for Validated Healthcare Directory Servers and Client applications, identifying the specific profiles, RESTful operations and search parameters that need to be supported.

Note: The individual Validated Healthcare Directory profiles identify the structural constraints, terminology bindings and invariants, however, implementers must refer to the conformance requirements for details on the RESTful operations, specific profiles and the search parameters applicable to each of the Validated Healthcare Directory actors.

----

Primary Authors: Dan Chaput, Alex Kontur, Brian Postlethwaite, Bob Dieterle

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
