#### Supported Searches

1. `GET [base]/InsurancePlan?insuranceplan-administered-by=[id]`

      *Support:* SHOULD support search by the [`insuranceplan-administered-by`](SearchParameter-insuranceplan-administered-by.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`, `organization-partof`
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-coverage-benefit-type=[code]`

      *Support:* SHALL support search by the [`insuranceplan-coverage-benefit-type`](SearchParameter-insuranceplan-coverage-benefit-type.html) parameter
   - including the modifiers:  `text`
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-coverage-limit-value=[prefix][number]|[system]|[code]`

      *Support:* MAY support search by the [`insuranceplan-coverage-limit-value`](SearchParameter-insuranceplan-coverage-limit-value.html) parameter   
   - including the comparators:  `eq`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`  
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-coverage-network=[id]`

      *Support:* SHALL support search by the [`insuranceplan-coverage-network`](SearchParameter-insuranceplan-coverage-network.html) parameter
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`, `organization-partof`
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-coverage-type=[code]`

      *Support:* SHALL support search by the [`insuranceplan-coverage-type`](SearchParameter-insuranceplan-coverage-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-endpoint=[id]`

      *Support:* SHOULD support search by the [`endpoint`](SearchParameter-insuranceplan-endpoint.html) parameter
   - with a target type:  `Endpoint`   
   - including these search paramaters which may be chained:  `endpoint-identifier`, `endpoint-connection-type`, `endpoint-organization`
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-general-cost-groupsize=[number]`

      *Support:* MAY support search by the [`insuranceplan-general-cost-groupsize`](SearchParameter-insuranceplan-general-cost-groupsize.html) parameter   
   - including the comparators:  `eq`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`  
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-general-cost-type=[code]`

      *Support:* MAY support search by the [`insuranceplan-general-cost-type`](SearchParameter-insuranceplan-general-cost-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-general-cost-value=[prefix][number]|[system]|[code]`

      *Support:* MAY support search by the [`insuranceplan-general-cost-value`](SearchParameter-insuranceplan-general-cost-value.html) parameter   
   - including the comparators:  `eq`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`  
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-name=[string]`

      *Support:* SHOULD support search by the [`insuranceplan-name`](SearchParameter-insuranceplan-name.html) parameter  
   - including the modifiers:  `exact`, `contains`   
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-owned-by=[id]`

      *Support:* SHALL support search by the [`insuranceplan-owned-by`](SearchParameter-insuranceplan-owned-by.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`, `organization-partof`
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-plan-coverage-area=[id]`

      *Support:* SHOULD support search by the [`insuranceplan-plan-coverage-area`](SearchParameter-insuranceplan-plan-coverage-area.html) parameter
   - with a target type:  `Location`   
   - including these search paramaters which may be chained:  `location-identifier`, `location-contains`
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-plan-identifier=[code]`

      *Support:* SHALL support search by the [`insuranceplan-plan-identifier`](SearchParameter-insuranceplan-plan-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-plan-network=[id]`

      *Support:* SHALL support search by the [`insuranceplan-plan-network`](SearchParameter-insuranceplan-plan-network.html) parameter
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`, `organization-partof`
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-plan-type=[code]`

      *Support:* SHALL support search by the [`insuranceplan-plan-type`](SearchParameter-insuranceplan-plan-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-product-coverage-area=[id]`

      *Support:* SHOULD support search by the [`insuranceplan-product-coverage-area`](SearchParameter-insuranceplan-product-coverage-area.html) parameter
   - with a target type:  `Location`   
   - including these search paramaters which may be chained:  `location-identifier`, `location-contains`
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-product-identifier=[code]

      *Support:* SHALL support search by the [`insuranceplan-product-identifier`](SearchParameter-insuranceplan-product-identifier.html) parameter
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-product-network=[id]`

      *Support:* SHALL support search by the [`insuranceplan-product-network`](SearchParameter-insuranceplan-product-network.html) parameter
   - with a target type:  `Organization`
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`, `organization-partof`
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-product-type=[code]`

      *Support:* SHALL support search by the [`insuranceplan-product-type`](SearchParameter-insuranceplan-product-type.html) parameter
   - including the modifiers:  `text`
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-specific-cost-benefit-type=[code]`

      *Support:* SHOULD support search by the [`insuranceplan-specific-cost-benefit-type`](SearchParameter-insuranceplan-specific-cost-benefit-type.html) parameter
   - including the modifiers:  `text`
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-specific-cost-category=[code]`

      *Support:* SHOULD support search by the [`insuranceplan-specific-cost-category`](SearchParameter-insuranceplan-specific-cost-category.html) parameter
   - including the modifiers:  `text`
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-specific-cost-cost-type=[code]`

      *Support:* MAY support search by the [`insuranceplan-specific-cost-cost-type`](SearchParameter-insuranceplan-specific-cost-cost-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-specific-cost-value=[prefix][number]|[system]|[code]`

      *Support:* MAY support search by the [`insuranceplan-specific-cost-value`](SearchParameter-insuranceplan-specific-cost-value.html) parameter   
   - including the comparators:  `eq`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`  
<hr />
1. `GET [base]/InsurancePlan?insuranceplan-status=[code]`

      *Support:* SHALL support search by the [`insuranceplan-status`](SearchParameter-insuranceplan-status.html) parameter

<hr />
