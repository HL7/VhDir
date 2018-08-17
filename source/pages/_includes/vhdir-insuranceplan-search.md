#### Supported Searches

1. `GET [base]/InsurancePlan?product-coveragearea=[id]`

      *Support:* SHOULD support search by the [`insuranceplan-product-coverage-area`](SearchParameter-searchparameter-insuranceplan-product-coverage-area.html) parameter 
   - with a target type:  `Location`   
   - including these search paramaters which may be chained:  `identifier`, `region` 
<hr />
1. `GET [base]/InsurancePlan?administered-by=[id]`

      *Support:* SHOULD support search by the [`administered-by`](SearchParameter-searchparameter-insuranceplan-administered-by.html) parameter 
   - with a target type:  `Organization` 
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `identifier`, `name`, `partof` 
<hr />
1. `GET [base]/InsurancePlan?coverage-benefit-type=[code]`

      *Support:* SHALL support search by the [`insuranceplan-coverage-benefit-type`](SearchParameter-searchparameter-insuranceplan-coverage-benefit-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/InsurancePlan?coverage-limit-vaue=[prefix][number]|[system]|[code]`

      *Support:* MAY support search by the [`insuranceplan-coverage-limit-value`](SearchParameter-searchparameter-insuranceplan-coverage-limit-value.html) parameter   
   - including the comparators:  `eq`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`  
<hr />
1. `GET [base]/InsurancePlan?coverage-network=[id]`

      *Support:* SHALL support search by the [`insuranceplan-coverage-network`](SearchParameter-searchparameter-insuranceplan-coverage-network.html) parameter 
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `identifier`, `name`, `partof` 
<hr />
1. `GET [base]/InsurancePlan?coverage-type=[code]`

      *Support:* SHALL support search by the [`insuranceplan-coverage-type`](SearchParameter-searchparameter-insuranceplan-coverage-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/InsurancePlan?endpoint=[id]`

      *Support:* SHOULD support search by the [`endpoint`](SearchParameter-searchparameter-insuranceplan-endpoint.html) parameter 
   - with a target type:  `Endpoint`   
   - including these search paramaters which may be chained:  `identifier`, `connection-type`, `organization` 
<hr />
1. `GET [base]/InsurancePlan?general-cost-groupsize=[number]`

      *Support:* MAY support search by the [`insuranceplan-general-cost-groupsize`](SearchParameter-searchparameter-insuranceplan-general-cost-groupsize.html) parameter   
   - including the comparators:  `eq`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`  
<hr />
1. `GET [base]/InsurancePlan?general-costs-type=[code]`

      *Support:* MAY support search by the [`insuranceplan-general-cost-type`](SearchParameter-searchparameter-insuranceplan-general-cost-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/InsurancePlan?general-costs-value=[prefix][number]|[system]|[code]`

      *Support:* MAY support search by the [`insuranceplan-general-cost-value`](SearchParameter-searchparameter-insuranceplan-general-cost-value.html) parameter   
   - including the comparators:  `eq`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`  
<hr />
1. `GET [base]/InsurancePlan?name=[string]`

      *Support:* SHOULD support search by the [`name`](SearchParameter-searchparameter-insuranceplan-name.html) parameter  
   - including the modifiers:  `exact`, `contains`   
<hr />
1. `GET [base]/InsurancePlan?owned-by=[id]`

      *Support:* SHALL support search by the [`owned-by`](SearchParameter-searchparameter-insuranceplan-owned-by.html) parameter 
   - with a target type:  `Organization` 
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`, `organization-partof` 
<hr />
1. `GET [base]/InsurancePlan?plan-coveragearea=[id]`

      *Support:* SHOULD support search by the [`insuranceplan-plan-coverage-area`](SearchParameter-searchparameter-insuranceplan-plan-coverage-area.html) parameter 
   - with a target type:  `Location`   
   - including these search paramaters which may be chained:  `identifier`, `region` 
<hr />
1. `GET [base]/InsurancePlan?plan-identifier=[code]`

      *Support:* SHALL support search by the [`insuranceplan-plan-identifier`](SearchParameter-searchparameter-insuranceplan-plan-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/InsurancePlan?plan-network=[id]`

      *Support:* SHALL support search by the [`insuranceplan-plan-network`](SearchParameter-searchparameter-insuranceplan-plan-network.html) parameter 
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `identifier`, `name`, `partof` 
<hr />
1. `GET [base]/InsurancePlan?plan-type=[code]`

      *Support:* SHALL support search by the [`insuranceplan-plan-type`](SearchParameter-searchparameter-insuranceplan-plan-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/InsurancePlan?identifier=[code]`

      *Support:* SHALL support search by the [`product-identifier`](SearchParameter-searchparameter-insuranceplan-product-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/InsurancePlan?network=[id]`

      *Support:* SHALL support search by the [`insuranceplan-product-network`](SearchParameter-searchparameter-insuranceplan-product-network.html) parameter 
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `identifier`, `name`, `partof` 
<hr />
1. `GET [base]/InsurancePlan?type=[code]`

      *Support:* SHALL support search by the [`product-type`](SearchParameter-searchparameter-insuranceplan-product-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/InsurancePlan?specific-costs-benefit-type=[code]`

      *Support:* SHOULD support search by the [`insuranceplan-specific-cost-benefit-type`](SearchParameter-searchparameter-insuranceplan-specific-cost-benefit-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/InsurancePlan?specific-costs-category=[code]`

      *Support:* SHOULD support search by the [`insuranceplan-specific-cost-category`](SearchParameter-searchparameter-insuranceplan-specific-cost-category.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/InsurancePlan?specific-costs-cost-type=[code]`

      *Support:* MAY support search by the [`insuranceplan-specific-cost-cost-type`](SearchParameter-searchparameter-insuranceplan-specific-cost-cost-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/InsurancePlan?specific-costs-value=[prefix][number]|[system]|[code]`

      *Support:* MAY support search by the [`insuranceplan-specific-cost-value`](SearchParameter-searchparameter-insuranceplan-specific-cost-value.html) parameter   
   - including the comparators:  `eq`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`  
<hr />
1. `GET [base]/InsurancePlan?status=[code]`

      *Support:* SHALL support search by the `status` parameter: `http://hl7.org/fhir/SearchParameter/InsurancePlan-status`
<hr />