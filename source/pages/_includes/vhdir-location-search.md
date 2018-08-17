#### Supported Searches

1. `GET [base]/Location?accessibility=[code]`

      *Support:* MAY support search by the [`location-accessibility`](SearchParameter-searchparameter-location-accessibility.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Location?address=[string]`

      *Support:* SHALL support search by the [`address`](SearchParameter-searchparameter-location-address.html) parameter  
   - including the modifiers:  `contains`, `exact`   
<hr />
1. `GET [base]/Location?endpoint=[id]`

      *Support:* SHOULD support search by the [`endpoint`](SearchParameter-searchparameter-location-endpoint.html) parameter
   - with a target type:  `Endpoint`   
   - including these search paramaters which may be chained:  `identifier`, `connection-type`, `organization`
<hr />
1. `GET [base]/Location?identifier=[code]`

      *Support:* SHALL support search by the [`identifier`](SearchParameter-searchparameter-location-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/Location?identifier-assigner=[id]`

      *Support:* MAY support search by the [`location-identifier-assigner`](SearchParameter-searchparameter-location-identifier-assigner.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `identifier`, `name`
<hr />
1. `GET [base]/Location?location-new-patient=[code]`

      *Support:* SHOULD support search by the [`location-new-patient`](SearchParameter-searchparameter-location-new-patient.html) parameter     
<hr />
1. `GET [base]/Location?location-new-patient-network=[id]`

      *Support:* SHOULD support search by the [`location-new-patient-network`](SearchParameter-searchparameter-location-new-patient-network.html) parameter
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `identifier`, `name`, `partof`
<hr />
1. `GET [base]/Location?organization=[id]`

      *Support:* SHALL support search by the [`organization`](SearchParameter-searchparameter-location-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `identifier`, `name`, `address`, `partof`, `type`
<hr />
1. `GET [base]/Location?partof=[id]`

      *Support:* SHOULD support search by the [`partof`](SearchParameter-searchparameter-location-partof.html) parameter
   - with a target type:  `Location`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `identifier`, `type`, `address`, `organization`
<hr />
1. `GET [base]/Location?location-organization=[id]`

      *Support:* SHALL support search by the [`location-organization`](SearchParameter-searchparameter-location-organization.html) parameter
<hr />
1. `GET [base]/Location?location-partof=[id]`

      *Support:* SHOULD support search by the [`location-partof`](SearchParameter-searchparameter-location-partof.html) parameter
<hr />
1. `GET [base]/Location?location-region=[uri]`

      *Support:* MAY support search by the [`location-region`](SearchParameter-searchparameter-location-region.html) parameter   
<hr />
1. `GET [base]/Location?status=[code]`

      *Support:* SHALL support search by the `status` parameter: `http://hl7.org/fhir/SearchParameter/Location-status`
<hr />
1. `GET [base]/Location?type=[code]`

      *Support:* SHALL support search by the [`type`](SearchParameter-searchparameter-location-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Location?location-status=[code]`

      *Support:* SHALL support search by the [`location-status`](SearchParameter-searchparameter-location-status.html) parameter
<hr />
1. `GET [base]/Location?location-type=[code]`

      *Support:* SHALL support search by the [`location-type`](SearchParameter-searchparameter-location-type.html) parameter
<hr />
1. `GET [base]/Location?location-via-intermediary=[id]`

      *Support:* MAY support search by the [`location-via-intermediary`](SearchParameter-searchparameter-location-via-intermediary.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />
