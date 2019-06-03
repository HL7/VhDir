#### Supported Searches

1. `GET [base]/InsurancePlan?administered-by=[id]`

      *Support:* SHOULD support search by the [`administered-by`](SearchParameter-insuranceplan-administered-by.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`
   - including these search paramaters which may be chained:  `administered-by.identifier`, `administered-by.name`, `administered-by.partof`
<hr />
1. `GET [base]/InsurancePlan?coverage-benefit-type=[code]`

      *Support:* SHALL support search by the [`coverage-benefit-type`](SearchParameter-insuranceplan-coverage-benefit-type.html) parameter
   - including the modifiers:  `text`
<hr />
1. `GET [base]/InsurancePlan?coverage-limit-value=[prefix][number]|[system]|[code]`

      *Support:* MAY support search by the [`coverage-limit-value`](SearchParameter-insuranceplan-coverage-limit-value.html) parameter   
   - including the comparators:  `eq`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`  
<hr />
1. `GET [base]/InsurancePlan?coverage-network=[id]`

      *Support:* SHALL support search by the [`coverage-network`](SearchParameter-insuranceplan-coverage-network.html) parameter
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `coverage-network.identifier`, `coverage-network.name`, `coverage-network.partof`
<hr />
1. `GET [base]/InsurancePlan?coverage-type=[code]`

      *Support:* SHALL support search by the [`coverage-type`](SearchParameter-insuranceplan-coverage-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/InsurancePlan?endpoint=[id]`

      *Support:* SHOULD support search by the [`endpoint`](SearchParameter-insuranceplan-endpoint.html) parameter
   - with a target type:  `Endpoint`   
   - including these search paramaters which may be chained:  `endpoint.identifier`, `endpoint.connection-type`, `endpoint.organization`
<hr />
1. `GET [base]/InsurancePlan?general-cost-groupsize=[number]`

      *Support:* MAY support search by the [`general-cost-groupsize`](SearchParameter-insuranceplan-general-cost-groupsize.html) parameter   
   - including the comparators:  `eq`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`  
<hr />
1. `GET [base]/InsurancePlan?general-cost-type=[code]`

      *Support:* MAY support search by the [`general-cost-type`](SearchParameter-insuranceplan-general-cost-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/InsurancePlan?general-cost-value=[prefix][number]|[system]|[code]`

      *Support:* MAY support search by the [`general-cost-value`](SearchParameter-insuranceplan-general-cost-value.html) parameter   
   - including the comparators:  `eq`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`  
<hr />
1. `GET [base]/InsurancePlan?name=[string]`

      *Support:* SHOULD support search by the [`name`](SearchParameter-insuranceplan-name.html) parameter  
   - including the modifiers:  `exact`, `contains`   
<hr />
1. `GET [base]/InsurancePlan?owned-by=[id]`

      *Support:* SHALL support search by the [`owned-by`](SearchParameter-insuranceplan-owned-by.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `owned-by.identifier`, `owned-by.name`, `owned-by.partof`
<hr />
1. `GET [base]/InsurancePlan?plan-coverage-area=[id]`

      *Support:* SHOULD support search by the [`plan-coverage-area`](SearchParameter-insuranceplan-plan-coverage-area.html) parameter
   - with a target type:  `Location`   
   - including these search paramaters which may be chained:  `plan-coverage-area.identifier`, `plan-coverage-area.contains`
<hr />
1. `GET [base]/InsurancePlan?plan-identifier=[code]`

      *Support:* SHALL support search by the [`plan-identifier`](SearchParameter-insuranceplan-plan-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/InsurancePlan?plan-network=[id]`

      *Support:* SHALL support search by the [`plan-network`](SearchParameter-insuranceplan-plan-network.html) parameter
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `plan-network.identifier`, `plan-network.name`, `plan-network.partof`
<hr />
1. `GET [base]/InsurancePlan?plan-type=[code]`

      *Support:* SHALL support search by the [`plan-type`](SearchParameter-insuranceplan-plan-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/InsurancePlan?product-coverage-area=[id]`

      *Support:* SHOULD support search by the [`product-coverage-area`](SearchParameter-insuranceplan-product-coverage-area.html) parameter
   - with a target type:  `Location`   
   - including these search paramaters which may be chained:  `product-coverage-area.identifier`, `product-coverage-area.contains`
<hr />
1. `GET [base]/InsurancePlan?product-identifier=[code]

      *Support:* SHALL support search by the [`product-identifier`](SearchParameter-insuranceplan-product-identifier.html) parameter
<hr />
1. `GET [base]/InsurancePlan?product-network=[id]`

      *Support:* SHALL support search by the [`product-network`](SearchParameter-insuranceplan-product-network.html) parameter
   - with a target type:  `Organization`
   - including these search paramaters which may be chained:  `product-network.identifier`, `product-network.name`, `product-network.partof`
<hr />
1. `GET [base]/InsurancePlan?product-type=[code]`

      *Support:* SHALL support search by the [`product-type`](SearchParameter-insuranceplan-product-type.html) parameter
   - including the modifiers:  `text`
<hr />
1. `GET [base]/InsurancePlan?specific-cost-benefit-type=[code]`

      *Support:* SHOULD support search by the [`specific-cost-benefit-type`](SearchParameter-insuranceplan-specific-cost-benefit-type.html) parameter
   - including the modifiers:  `text`
<hr />
1. `GET [base]/InsurancePlan?specific-cost-category=[code]`

      *Support:* SHOULD support search by the [`specific-cost-category`](SearchParameter-insuranceplan-specific-cost-category.html) parameter
   - including the modifiers:  `text`
<hr />
1. `GET [base]/InsurancePlan?specific-cost-cost-type=[code]`

      *Support:* MAY support search by the [`specific-cost-cost-type`](SearchParameter-insuranceplan-specific-cost-cost-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/InsurancePlan?specific-cost-value=[prefix][number]|[system]|[code]`

      *Support:* MAY support search by the [`specific-cost-value`](SearchParameter-insuranceplan-specific-cost-value.html) parameter   
   - including the comparators:  `eq`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`  
<hr />
1. `GET [base]/InsurancePlan?status=[code]`

      *Support:* SHALL support search by the [`status`](SearchParameter-insuranceplan-status.html) parameter

<hr />
