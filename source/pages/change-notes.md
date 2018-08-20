---
title: Change Notes
layout: default
active: change notes
topofpage: true
sectionnumbering: true
F: http://build.fhir.org/
---

The Validated Healthcare Directory Implementation guide was developed under the [ONC Healthcare Directory Initiative (HcDir)](https://oncprojectracking.healthit.gov/wiki/display/TechLabSC/Healthcare+Directory). HcDir was a US initiative sponsored by the Office of the National Coordinator (ONC) and Federal Health Architecture (FHA) which aimed to create FHIR profiles for access to a national validated dataset of healthcare directory data.

This implementation guide was was initially developed under FHIR Release 3 (STU) and ported into FHIR Release 4 (STU), and considered the Provider Directory resources created under [The Argonaut Project](http://argonautwiki.hl7.org/index.php?title=Main_Page).

Changes Since the January 2018 for comment ballot:

* Inclusion of many guidance pages
* Refinement of profiles based on ballot feedback
* Alignment with R4 core updates
  * OrganizationRole -> OrganizationAffiliation
  * ProductPlan -> InsurancePlan
  * Location boundaries using R4 standard extension
* Inclusion of many missing valuesets
* Completion of unfinished definitions

A future iteration of this guide will align with the US Core R4 build, and provide tight bindings for US usage, along with the current international profile bindings.
