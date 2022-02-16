<!-- ---
title: General Security Considerations
layout: default
active: security
topofpage: true
sectionnumbering: true
F: http://build.fhir.org/
--- -->

The following are the VhDir security considerations that implementers should follow:
* All implementers of FHIR servers and clients should pay attention to [FHIR Security](http://hl7.org/fhir/security.html) considerations.
* In addition to the [FHIR Security](http://hl7.org/fhir/security.html) considerations, the VhDir requests need to contain specific information about VhDir client identity and organization information.
* Providing this information using FHIR Search APIs is very cumbersome and is not necessary. This kind of information can be collected by the VhDir Authorization Server during application registration and avoid repeating the information on each request.
* These mechanisms are outlined in detail in the [SMART Backend Services Authorization Guide](http://docs.smarthealthit.org/authorization/backend-services/).


The following are security conformance requirements for VhDir actors:
* VhDir actors *SHALL* use the [SMART Backend Services Authorization Guide] to collect the necessary requestor information appropriate for making the VhDir data request.
* VhDir actors *SHALL* reference a single time source to establish a common time base for security auditing across the system.
* VhDir actors *SHALL* use the [AuditEvent] resource to capture audit logs of the various transactions. VhDir actors *SHOULD* capture as many AuditEvent resource data elements as appropriate based on requirements of FHIR [Audit Logging] and local policies.
* VhDir transactions *SHALL* use TLS version 1.2 or higher to secure the transmission channel unless the transmission is taking place over a more secure network.(Using TLS even within a secured network environment is still encouraged to provide defense in depth.) US Federal systems implementing VhDir actors *SHOULD* conform with FIPS PUB 140-2.
* VhDir actors *SHALL* conform to [FHIR Communications] requirements.
* VhDir actors *SHOULD* retain Provenance information using the [FHIR Provenance] resource.


The following are security conformance requirements for the overall program/system:

* VhDir implementers *SHOULD* establish a risk analysis and management regime that conforms with HIPAA security regulatory requirements. In addition, implementers in the US Federal systems *SHOULD* conform with the risk management and mitigation requirements defined in NIST 800 series documents. This *SHOULD* include security category assignment in accordance with NIST 800-60 vol. 2 Appendix D.14. The coordination of risk management and the related security and privacy controls – policies, administrative practices, and technical controls – *SHOULD* be defined in the Business Associate Agreements.
* The time service used for auditing *SHOULD* be documented in the Business Associate Agreements.



  [FHIR Communications]: http://hl7.org/fhir/STU3/security.html#http
  [Smart On FHIR]: http://fhir-docs.smarthealthit.org/argonaut-dev/authorization/backend-services/
  [FHIR Security Labels]: http://hl7.org/fhir/STU3/security-labels.html
  [General Security Considerations]: #general-security-considerations
  [FHIR Provenance]: http://hl7.org/fhir/STU3/provenance.html
  [FHIR Digital Signatures]: http://hl7.org/fhir/STU3/security.html#digital%20signatures
  [SMART Backend Services Authorization Guide]:http://docs.smarthealthit.org/authorization/backend-services/

  [security considerations]: http://hl7.org/fhir/STU3/security.html
  [Communications]: http://hl7.org/fhir/STU3/security.html#http
  [Authentication]: http://hl7.org/fhir/STU3/security.html#authentication
  [Authorization/Access Control]: http://hl7.org/fhir/STU3/security.html#authorization/access%20control
  [Audit Logging]: http://hl7.org/fhir/STU3/security.html#audit%20logging
  [Digital Signatures]: http://hl7.org/fhir/STU3/security.html#digital%20signatures
  [Security Labels]: http://hl7.org/fhir/STU3/security-labels.html
  [Narrative]: http://hl7.org/fhir/STU3/security.html#narrative
  [AuditEvent]: http://hl7.org/fhir/STU3/auditevent.html
  [Audit Logging]: http://hl7.org/fhir/STU3/security.html#audit
  [Consent]: http://hl7.org/fhir/STU3/consent.html
