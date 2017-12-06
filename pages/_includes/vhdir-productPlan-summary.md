#### Complete Summary of the Mandatory Requirements

1.  One owner in `productPlan.ownedBy`
1.  One administrator in `productPlan.administeredBy`
1.  At least one covered benefit described in `productPlan.productCoverage`. This attribute consists of a number of other mandatory attributes:
    1.  One type in `productPlan.productCoverage.coverageType`
    1.  At least one benefit described in `productPlan.productCoverage.benefits`
    1.  One type in `productPlan.productCoverage.benefits.type`
    1.  At least one specific benefit described in `productPlan.productCoverage.benefits.benefitList`
    1.  One description of the benefit in `productPlan.productCoverage.benefits.benefitList.description`
1.  At least one cost described in `productPlan.plan`.
    1.  For each cost in `productPlan.benefitCategory.benefit.costs`, one type in `productPlan.benefitCategory.benefit.costs.type`