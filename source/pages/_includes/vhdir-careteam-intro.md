This profile sets minimum expectations for searching for and fetching information associated with a care team. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the CareTeam resource when using this profile.

**Background & Scope**

A care team consists of the providers and/or organizations responsible for the care of a patient. Individuals participating on a VHDir CareTeam SHALL be represented through an associated role. Therefore, this profile removes references to the Practitioner resource in `CareTeam.participant.member`. For example, Dr. Smith (an individual) does not participate on a care team. Rather, Dr. Smith in his role as a provider at Acme Hospital participates on a care team.

A care team may be functionally "empty," i.e. the roles on the care team are not filled by individuals. For example, a care team may be comprised of a primary care provider role, care coordinator role, and specialist role without indicating the individuals filling those roles. This enables entities to describe existing care teams while masking the identity of the individuals/organizations that are involved, or to represent standing care teams that are filled by individuals on an ad hoc basis in response to a condition/event.

This profile modifies the base CareTeam resource in the following manner:

*  Constrains the cardinality of `careTeam.status` (1..1), `careTeam.category` (1..*), `careTeam.context` (0..0), `careTeam.subject` (0..0), `careTeam.onBehalfOf` (0..0), `careTeam.managingOrganization` (0..1), `careTeam.reasonCode` (0..0), `careTeam.reasonReference` (0..0), `careTeam.telecom.system` (1..1), and `careTeam.telecom.value` (1..1)

*   Modifies the data type of careTeam.note.author (removes references to Patient and RelatedPerson resources)

*   Modifies the data type of CareTeam.participant.member (removes references to Patient, RelatedPerson, and Practitioner resources)

*  All references SHALL conform to the appropriate Validated Healthcare Directory Implementation Guide profile

*  Adds extensions:

1.  [Identifier status](StructureDefinition-identifier-status.html) (1..1) - indicates the status of a care team's identifier
1.  [Via intermediary](StructureDefinition-contactpoint-viaintermediary.html) (0..1) - a reference to an alternative point of contact for this care team
1.  [Available time](StructureDefinition-contactpoint-availabletime.html) (0..*) - indicates when a care team is available for contact
1.  [Alias](StructureDefinition-careteam-alias.html) (0..*) - indicates alternate names by which the care team is known
1.  [Location](StructureDefinition-location-reference.html) (0..*) - reference(s) to the location resource, indicating the location(s) at which the care team operates or delivers services
1.  [Service](StructureDefinition-healthcareservice-reference.html) (0..*) - reference(s) to the healthcareService resource, indicating the services offered by the care team
1.  [Endpoint](StructureDefinition-endpoint-reference.html) (0..*) - reference(s) to the endpoint resource, indicating technical endpoints for the care team independent of its members, affiliated organizations, etc.
1.  [Restriction](StructureDefinition-usage-restriction.html) (0..*) - indicates whether disclosure of any data associated with a care team is restricted

*  Adds new value sets/updates value set bindings:

TBD



**Examples:**

The following are example uses for the vhdir-careteam profile:

-  [A cardiology care team at Founding Fathers Memorial Hospital](CareTeam-cardiologycareteam1.html)


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each CareTeam must have:

1.  One status code in `careTeam.status`
1.  At least one type of care team in `careTeam.category`
