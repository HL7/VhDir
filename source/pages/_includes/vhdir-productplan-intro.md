This profile sets minimum expectations for searching for and fetching information associated with a health insurance product/plan. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the productPlan resource when using this profile.

**Background & Scope**

A product is a discrete package of health insurance coverage benefits that are offered under a particular network type. A given payer's products typically differ by network type and/or coverage benefits. A plan pairs the health insurance coverage benefits under a product with the particular cost sharing structure offered to a consumer. A given product may comprise multiple plans. 

ProductPlan describes a health insurance offering comprised of a list of covered benefits (i.e. the product), costs associated with those benefits (i.e. the plan), and additional information about the offering, such as who it is owned and administered by, a coverage area, contact information, etc.


**Examples:**

The following are example uses for the vhdir-productplan profile:

-  TBD


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each productPlan resource must have:

1.  At least one covered benefit described in `productPlan.productCoverage`. This attribute consists of a number of other mandatory attributes:
    1.  One type in `productPlan.productCoverage.coverageType`
    1.  At least one benefit described in `productPlan.productCoverage.benefits`
    1.  One type in `productPlan.productCoverage.benefits.type`
    1.  At least one specific benefit described in `productPlan.productCoverage.benefits.benefitList`
    1.  One description of the benefit in `productPlan.productCoverage.benefits.benefitList.description`
1.  At least one cost described in `productPlan.plan`.
    1.  For each cost in `productPlan.benefitCategory.benefit.costs`, one type in `productPlan.benefitCategory.benefit.costs.type`


**Profile specific implementation guidance:**

- TBD


**Terminology**

TBD
