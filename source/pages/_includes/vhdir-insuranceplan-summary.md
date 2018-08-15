#### Complete Summary of the Mandatory Requirements

1.  At least one covered benefit described in `insurancePlan.productCoverage`. This attribute consists of a number of other mandatory attributes:
    1.  One type in `insurancePlan.productCoverage.coverageType`
    1.  At least one benefit described in `insurancePlan.productCoverage.benefits`
    1.  One type in `insurancePlan.productCoverage.benefits.type`
    1.  At least one specific benefit described in `insurancePlan.productCoverage.benefits.benefitList`
    1.  One description of the benefit in `insurancePlan.productCoverage.benefits.benefitList.description`
1.  At least one cost described in `insurancePlan.plan`.
    1.  For each cost in `insurancePlan.benefitCategory.benefit.costs`, one type in `insurancePlan.benefitCategory.benefit.costs.type`