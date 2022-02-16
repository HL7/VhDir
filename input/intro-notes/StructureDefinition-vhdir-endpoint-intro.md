This profile sets minimum expectations for searching for and fetching information associated with an electronic endpoint. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the Endpoint resource when using this profile.

**Background & Scope**

An endpoint describes the technical details of a location that can be connected to for the delivery/retrieval of information.

This profile modifies the base Endpoint resource in the following manner:

*  Constrains the cardinality of `endpoint.contact` (0..1), `endpoint.contact.system` (1..1), and `endpoint.contact.value` (1..1)

*  All references SHALL conform to the appropriate Validated Healthcare Directory Implementation Guide profile

*  Adds extensions:

1.  [Identifier status](StructureDefinition-identifier-status.html) (1..1) - indicates the status of an endpoint's identifier
1.  [Via intermediary](StructureDefinition-contactpoint-viaintermediary.html) (0..1) - a reference to an alternative point of contact for this endpoint
1.  [Available time](StructureDefinition-contactpoint-availabletime.html) (0..*) - indicates when the point of contact for an endpoint is available
1.  [UseCase](StructureDefinition-endpoint-usecase.html) (0..*) - an enumeration of the specific use cases (service descriptions) supported by the endpoint
1.  [Rank](StructureDefinition-endpoint-rank.html) (0..1) - an indication of the preferred order for connecting to an endpoint when multiple endpoints capable of transferring the same content are listed
1.  [DigitalCertificate](StructureDefinition-digitalcertificate.html) (0..*) - a digital certificate associated with the endpoint
1.  [Restriction](StructureDefinition-usage-restriction.html) (0..*) - indicates whether disclosure of any data associated with an endpoint is restricted

<!-- *  Adds new value sets/updates value set bindings:

TBD -->

**Examples:**

The following are example uses for the vhdir-endpoint profile:

-  [A Direct address used by cardiologists at the Founding Fathers Memorial Hospital Heart and Vascular Institute](Endpoint-direct321.html)


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each endpoint must have:

1.  A status code in `endpoint.status`
1.  A connectionType code in `endpoint.connectionType`
1.  At least one indication of the type of content the endpoint supports in `endpoint.payloadType`
1.  One technical address for connecting to the endpoint in `endpoint.address`


<!--**Profile specific implementation guidance:**

- TBD -->
