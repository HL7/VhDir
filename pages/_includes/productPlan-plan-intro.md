An extension to describe a health insurance plan. A plan pairs the health insurance coverage benefits under a product with the particular cost sharing structure offered to a consumer.

This extension consists of a number of tiers. The first tier includes general information about the plan, such as the type, a description, and premiums associated with the plan.
The second tier inidcates a general category of benefits.
The third tier indicates a specific benefit from that category.
The fourth tier indicates the costs associated with the specific benefit, including the amount, type, whether the cost applies to in-network or out-of-network care, and any additional information. 

Specific attributes include:
*  `plan.planType` - indicates the type of plan (e.g. bronze, silver, high deductible)
*  `plan.description` - provides additional descriptive information about the plan
*  `plan.premium` - indicates premiums associated with the plan
*  `plan.benefitCategory.category` - indicates a general category of benefits (e.g. medical, dental)
*  `plan.benefitCategory.benefit.type` - indicates a specific type of benefit (e.g. preventative, emergent care)
*  `plan.benefitCategory.benefit.costs.type` - indicates a type of cost associated with a specific benefit (e.g. copay, coinsurance)
*  `plan.benefitCategory.benefit.costs.applicability` - indicates whether the cost applies to in-network or out-of-network providers
*  `plan.benefitCategory.benefit.costs.qualifiers` - provides additional information about the cost (e.g. information about funding sources such as a health savings account)
*  `plan.benefitCategory.benefit.costs.value` - indicates the value of the cost associated with a benefit