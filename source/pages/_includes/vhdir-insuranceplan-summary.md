#### Complete Summary of the Mandatory Requirements

1.  A coded value in `InsurancePlan.status`
1.  A reference to an organization that issues the product/plan in `InsurancePlan.ownedBy`
1.  A reference to an organization that administers the product/plan in `InsurancePlan.administeredBy`
1.  For each set of coverage details, one coded type of coverage in `InsurancePlan.coverage.type`
1.  For each set of coverage details, at least one covered benefit in `InsurancePlan.coverage.benefit`, including a coded type of benefit in `InsurancePlan.coverage.benefit.type`
1.  For each set of specific costs associated with a Plan, a coded value indicating the general category of benefit the cost applies to in `InsurancePlan.plan.specificCost.category`
1.  For each set specific costs associated with a covered benefit, a coded type of benefit in `InsurancePlan.plan.specificCost.benefit.type`
1.  For each set of specific costs associated with covered benefits, a coded type of cost in `InsurancePlan.plan.specificCost.benefit.cost.type`