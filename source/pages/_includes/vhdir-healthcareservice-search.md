#### Supported Searches

1. `GET [base]/HealthcareService?active=[code]`

      *Support:* SHALL support search by the `active` parameter: `http://hl7.org/fhir/SearchParameter/HealthcareService-active`
<hr />
1. `GET [base]/HealthcareService?service-category=[code]`

      *Support:* SHALL support search by the [`service-category`](SearchParameter-healthcareservice-service-category.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/HealthcareService?characteristic=[code]`

      *Support:* MAY support search by the [`characteristic`](SearchParameter-healthcareservice-characteristic.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/HealthcareService?coverage-area=[id]`

      *Support:* SHOULD support search by the [`coverage-area`](SearchParameter-healthcareservice-coverage-area.html) parameter
   - with a target type:  `Location`   
   - including these search paramaters which may be chained:  `coverage-area.identifier`, `coverage-area.contains`
<hr />
1. `GET [base]/HealthcareService?eligibility=[code]`

      *Support:* SHOULD support search by the [`eligibility`](SearchParameter-healthcareservice-eligibility.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/HealthcareService?endpoint=[id]`

      *Support:* SHOULD support search by the [`endpoint`](SearchParameter-healthcareservice-endpoint.html) parameter
   - with a target type:  `Endpoint`   
   - including these search paramaters which may be chained:  `endpoint.identifier`, `endpoint.connection-type`, `endpoint.organization`
<hr />
1. `GET [base]/HealthcareService?identifier=[code]`

      *Support:* SHALL support search by the [`identifier`](SearchParameter-healthcareservice-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/HealthcareService?identifier-assigner=[id]`

      *Support:* MAY support search by the [`identifier-assigner`](SearchParameter-healthcareservice-identifier-assigner.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `identifier-assigner.identifier`, `identifier-assigner.name`
<hr />
1. `GET [base]/HealthcareService?location=[id]`

      *Support:* SHALL support search by the [`location`](SearchParameter-healthcareservice-location.html) parameter
   - with a target type:  `Location`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `location.identifier`, `location.type`, `location.address`, `location.organization`
<hr />
1. `GET [base]/HealthcareService?name=[string]`

      *Support:* SHOULD support search by the [`name`](SearchParameter-healthcareservice-name.html) parameter  
   - including the modifiers:  `exact`, `contains`   
<hr />
1. `GET [base]/HealthcareService?new-patient=[code]`

      *Support:* SHOULD support search by the [`new-patient`](SearchParameter-healthcareservice-new-patient.html) parameter     
<hr />
1. `GET [base]/HealthcareService?new-patient-network=[id]`

      *Support:* SHOULD support search by the [`new-patient-network`](SearchParameter-healthcareservice-new-patient-network.html) parameter
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `new-patient-network.identifier`, `new-patient-network.name`, `new-patient-network.partof`
<hr />
1. `GET [base]/HealthcareService?organization=[id]`

      *Support:* SHALL support search by the [`organization`](SearchParameter-healthcareservice-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `organization.identifier`, `organization.name`, `organization.address`, `organization.partof`, `organization-type`
<hr />
1. `GET [base]/HealthcareService?specialty=[code]`

      *Support:* SHOULD support search by the [`specialty`](SearchParameter-healthcareservice-specialty.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/HealthcareService?service-type=[code]`

      *Support:* SHOULD support search by the [`service-type`](SearchParameter-healthcareservice-service-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/HealthcareService?via-intermediary=[id]`


      *Support:* MAY support search by the [`via-intermediary`](SearchParameter-healthcareservice-via-intermediary.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />
