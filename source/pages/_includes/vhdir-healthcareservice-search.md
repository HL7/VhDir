#### Supported Searches

1. `GET [base]/HealthcareService?active=[code]`

      *Support:* SHALL support search by the `active` parameter: `http://hl7.org/fhir/SearchParameter/HealthcareService-active`
<hr />
1. `GET [base]/HealthcareService?service-category=[code]`

      *Support:* SHALL support search by the [`service-category`](SearchParameter-healthcareservice-service-category.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/HealthcareService?healthcareservice-characteristic=[code]`

      *Support:* MAY support search by the [`healthcareservice-characteristic`](SearchParameter-searchparameter-healthcareservice-characteristic.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/HealthcareService?healthcareservice-coverage-area=[id]`

      *Support:* SHOULD support search by the [`healthcareservice-coverage-area`](SearchParameter-searchparameter-healthcareservice-coverage-area.html) parameter
   - with a target type:  `Location`   
   - including these search paramaters which may be chained:  `location-identifier`, `location-contains`
<hr />
1. `GET [base]/HealthcareService?healthcareservice-eligibility=[code]`

      *Support:* SHOULD support search by the [`healthcareservice-eligibility`](SearchParameter-searchparameter-healthcareservice-eligibility.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/HealthcareService?healthcareservice-endpoint=[id]`

      *Support:* SHOULD support search by the [`healthcareservice-endpoint`](SearchParameter-searchparameter-healthcareservice-endpoint.html) parameter
   - with a target type:  `Endpoint`   
   - including these search paramaters which may be chained:  `endpoint-identifier`, `endpoint-connection-type`, `endpoint-organization`
<hr />
1. `GET [base]/HealthcareService?healthcareservice-identifier=[code]`

      *Support:* SHALL support search by the [`healthcareservice-identifier`](SearchParameter-searchparameter-healthcareservice-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/HealthcareService?healthcareservice-identifier-assigner=[id]`

      *Support:* MAY support search by the [`healthcareservice-identifier-assigner`](SearchParameter-searchparameter-healthcareservice-identifier-assigner.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`
<hr />
1. `GET [base]/HealthcareService?healthcareservice-location=[id]`

      *Support:* SHALL support search by the [`healthcareservice-location`](SearchParameter-searchparameter-healthcareservice-location.html) parameter
   - with a target type:  `Location`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `location-identifier`, `location-type`, `location-address`, `location-organization`
<hr />
1. `GET [base]/HealthcareService?healthcareservice-name=[string]`

      *Support:* SHOULD support search by the [`healthcareservice-name`](SearchParameter-searchparameter-healthcareservice-name.html) parameter  
   - including the modifiers:  `exact`, `contains`   
<hr />
1. `GET [base]/HealthcareService?healthcareservice-new-patient=[code]`

      *Support:* SHOULD support search by the [`healthcareservice-new-patient`](SearchParameter-searchparameter-healthcareservice-new-patient.html) parameter     
<hr />
1. `GET [base]/HealthcareService?healthcareservice-new-patient-network=[id]`

      *Support:* SHOULD support search by the [`healthcareservice-new-patient-network`](SearchParameter-searchparameter-healthcareservice-new-patient-network.html) parameter
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`, `organization-partof`
<hr />
1. `GET [base]/HealthcareService?healthcareservice-organization=[id]`

      *Support:* SHALL support search by the [`healthcareservice-organization`](SearchParameter-searchparameter-healthcareservice-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`, `organization-address`, `organization-partof`, `organization-type`
<hr />
1. `GET [base]/HealthcareService?healthcareservice-specialty=[code]`

      *Support:* SHOULD support search by the [`healthcareservice-specialty`](SearchParameter-searchparameter-healthcareservice-specialty.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/HealthcareService?service-type=[code]`

      *Support:* SHOULD support search by the [`service-type`](SearchParameter-healthcareservice-service-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/HealthcareService?healthcareservice-via-intermediary=[id]`


      *Support:* MAY support search by the [`healthcareservice-via-intermediary`](SearchParameter-searchparameter-healthcareservice-via-intermediary.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />
