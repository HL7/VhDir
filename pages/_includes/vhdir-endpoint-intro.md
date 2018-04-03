This profile sets minimum expectations for searching for and fetching information associated with an electronic endpoint. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the Endpoint resource when using this profile.

**Background & Scope**

An endpoint describes the technical details of a location that can be connected to for the delivery/retrieval of information.

This profile constrains `endpoint.contact` (only one contact point for an endpoint is permitted), and adds extensions for describing the types of services supported by the endpoint, ranking endpoints when there are multiple endpoints to connect to, and identifying a digital certificate associated with the endpoint.

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


**Profile specific implementation guidance:**

- TBD


**Extensions:**

1.  [UseCase](StructureDefinition-endpoint-usecase.html) (0..*) - an enumeration of the specific use cases (service descriptions) supported by the endpoint
1.  [Rank](StructureDefinition-endpoint-rank.html) (0..1) - an indication of the preferred order for connecting to an endpoint when multiple endpoints capable of transferring the same content are listed
1.  [DigitalCertificate](StructureDefinition-digitalcertificate.html) (0..*) - a digital certificate associated with the endpoint


**Terminology**

TBD

