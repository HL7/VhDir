#### Supported Searches

1. `GET [base]/HealthcareService?active=[code]`

      *Support:* SHALL support search by the `active` parameter: `http://hl7.org/fhir/SearchParameter/HealthcareService-active`
<hr />
1. `GET [base]/HealthcareService?category=[code]`

      *Support:* SHALL support search by the [`category`](SearchParameter-searchparameter-healthcareservice-category.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/HealthcareService?characteristic=[code]`

      *Support:* MAY support search by the [`characteristic`](SearchParameter-searchparameter-healthcareservice-characteristic.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/HealthcareService?coveragearea=[id]`

      *Support:* SHOULD support search by the [`healthcareservice-coverage-area`](SearchParameter-searchparameter-healthcareservice-coverage-area.html) parameter 
   - with a target type:  `Location`   
   - including these search paramaters which may be chained:  `identifier`, `region` 
<hr />
1. `GET [base]/HealthcareService?eligibility=[code]`

      *Support:* SHOULD support search by the [`healthcareservice-eligibility`](SearchParameter-searchparameter-healthcareservice-eligibility.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/HealthcareService?endpoint=[id]`

      *Support:* SHOULD support search by the [`endpoint`](SearchParameter-searchparameter-healthcareservice-endpoint.html) parameter 
   - with a target type:  `Endpoint`   
   - including these search paramaters which may be chained:  `identifier`, `connection-type`, `organization` 
<hr />
1. `GET [base]/HealthcareService?identifier=[code]`

      *Support:* SHALL support search by the [`identifier`](SearchParameter-searchparameter-healthcareservice-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/HealthcareService?identifier-assigner=[id]`

      *Support:* MAY support search by the [`healthcareservice-identifier-assigner`](SearchParameter-searchparameter-healthcareservice-identifier-assigner.html) parameter 
   - with a target type:  `Organization` 
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `identifier`, `name` 
<hr />
1. `GET [base]/HealthcareService?location=[id]`

      *Support:* SHALL support search by the [`location`](SearchParameter-searchparameter-healthcareservice-location.html) parameter 
   - with a target type:  `Location` 
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `identifier`, `type`, `address`, `organization` 
<hr />
1. `GET [base]/HealthcareService?name=[string]`

      *Support:* SHOULD support search by the [`name`](SearchParameter-searchparameter-healthcareservice-name.html) parameter  
   - including the modifiers:  `exact`, `contains`   
<hr />
1. `GET [base]/HealthcareService?new-patient=[code]`

      *Support:* SHOULD support search by the [`healthcareservice-new-patient`](SearchParameter-searchparameter-healthcareservice-new-patient.html) parameter     
<hr />
1. `GET [base]/HealthcareService?new-patient-network=[id]`

      *Support:* SHOULD support search by the [`healthcareservice-new-patient-network`](SearchParameter-searchparameter-healthcareservice-new-patient-network.html) parameter 
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `identifier`, `name`, `partof` 
<hr />
1. `GET [base]/HealthcareService?organization=[id]`

      *Support:* SHALL support search by the [`organization`](SearchParameter-searchparameter-healthcareservice-organization.html) parameter 
   - with a target type:  `Organization` 
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `identifier`, `name`, `address`, `partof`, `type` 
<hr />
1. `GET [base]/HealthcareService?specialty=[code]`

      *Support:* SHOULD support search by the [`healthcareservice-specialty`](SearchParameter-searchparameter-healthcareservice-specialty.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/HealthcareService?type=[code]`

      *Support:* SHOULD support search by the [`type`](SearchParameter-searchparameter-healthcareservice-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/HealthcareService?via-intermediary=[id]`

      *Support:* MAY support search by the [`healthcareservice-via-intermediary`](SearchParameter-searchparameter-healthcareservice-via-intermediary.html) parameter 
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />