This profile sets minimum expectations for searching for and fetching information associated with a health insurance product/plan. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the InsurancePlan resource when using this profile.

**Background & Scope**

A product is a discrete package of health insurance coverage benefits that are offered under a particular network type. A given payer's products typically differ by network type and/or covered benefits. A plan pairs a product's covered benefits with the particular cost sharing structure offered to a consumer. A given product may comprise multiple plans (i.e. each plan offers different cost sharing requirements for the same set of covered benefits). 

InsurancePlan describes a health insurance offering comprised of a list of covered benefits (i.e. the product), costs associated with those benefits (i.e. the plan), and additional information about the offering, such as who it is owned and administered by, a coverage area, contact information, etc.

This profile modifies the base InsurancePlan resource in the following manner:

*  Constrains the cardinality of `InsurancePlan.status` (1..1), `InsurancePlan.ownedBy` (1..1), `InsurancePlan.administeredBy` (1..1), `InsurancePlan.contact.name.family` (1..1), `InsurancePlan.contact.name.given` (1..*), `InsurancePlan.contact.telecom.system` (1..1), and `InsurancePlan.contact.telecom.value` (1..1)

*  All references SHALL conform to the appropriate Validated Healthcare Directory Implementation Guide profile

*  Adds extensions:

1.  [Identifier status](StructureDefinition-identifier-status.html) (1..1) - indicates the status of a product or plan's identifier
1.  [Via intermediary](StructureDefinition-contactpoint-viaintermediary.html) (0..1) - a reference to an alternative point of contact for this InsurancePlan
1.  [Available time](StructureDefinition-contactpoint-availabletime.html) (0..*) - indicates when the point of contact for an InsurancePlan is available
1.  [Restriction](StructureDefinition-usage-restriction.html) (0..*) - indicates whether disclosure of any data associated with a service is restricted

<!--- *  Adds new value sets/updates value set bindings:

TBD --->

**Examples:**

The following are example uses for the vhdir-insuranceplan profile:

-  [Patriot PPO Standard](InsurancePlan-insuranceplan1.html)


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.   

Each insurancePlan resource must have:

1.  A coded value in `InsurancePlan.status`
1.  A reference to an organization that issues the product/plan in `InsurancePlan.ownedBy`
1.  A reference to an organization that administers the product/plan in `InsurancePlan.administeredBy`
1.  For each set of coverage details, one coded type of coverage in `InsurancePlan.coverage.type`
1.  For each set of coverage details, at least one covered benefit in `InsurancePlan.coverage.benefit`, including a coded type of benefit in `InsurancePlan.coverage.benefit.type`
1.  For each set of specific costs associated with a Plan, a coded value indicating the general category of benefit the cost applies to in `InsurancePlan.plan.specificCost.category`
1.  For each set specific costs associated with a covered benefit, a coded type of benefit in `InsurancePlan.plan.specificCost.benefit.type`
1.  For each set of specific costs associated with covered benefits, a coded type of cost in `InsurancePlan.plan.specificCost.benefit.cost.type`
