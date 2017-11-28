This profile sets minimum expectations for searching for and fetching information associated with a care team. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the CareTeam resource when using this profile.

**Background & Scope**

A care team consists of the providers and/or organizations responsible for the care of a patient. It is defined not as a collection of individuals and organizations, but as a collection of roles; each member of a care team is represented through an associated role. Therefore, this profile removes references to practitioner and organization resources in `careTeam.member` and adds references to practitionerRole and organizationRole. For example, Dr. Smith (an individual) does not participate on a care team. Rather, Dr. Smith in his role as a provider at Acme Hospital participates on a care team.

A care team may be functionally "empty," i.e. the roles on the care team are not filled by individuals or organizations. For example, a care team may be comprised of a primary care provider, care coordinator, and specialist without indicating the individuals filling those roles. This enables entities to describe existing care teams while masking the identity of the indivudals/organizations that are involved, or to represent standing care teams that are filled on an ad hoc basis in response to a condition/event.

This profile removes `careTeam.subject`, `careTeam.context`, `careTeam.reasonReference`, and references to patient and relatedPerson resources in `careTeam.member` because maintaining patient information is out of scope for this implementation guide. It also constrains the number of organizations responsible for managing a care team to one.


**Examples:**

The following are example uses for the vhdir-careteam profile:

-  TBD


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each CareTeam must have:

1.  At least one type of care team in `careTeam.category`
1.  A period for which the care team is active in `careTeam.period`


**Profile specific implementation guidance:**

- TBD


**Extensions:**

1.  Restriction (0..*) - indicates restrictions on the use/release of information associated with the care team
1.  Alias (0..*) - indicates alternate names by which the care team is known
1.  Location (0..*) - reference(s) to the location resource, indicating the location(s) at which the care team operates or delivers services
1.  Service (0..*) - reference(s) to the healthcareService resource, indicating the services offered by the care team
1.  Endpoint (0..*) - reference(s) to the endpoint resource, indicating technical endpoints for the care team independent of its members, affiliated organizations, etc.
1.  Mode (0..1) - indicates whether the care team is an instance or kind of care team


**Terminology**

TBD