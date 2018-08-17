#### Supported Searches

1. `GET [base]/Endpoint?connection-type=[code]`

      *Support:* SHALL support search by the [`connection-type`](SearchParameter-searchparameter-endpoint-connection-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Endpoint?identifier=[code]`

      *Support:* SHALL support search by the [`identifier`](SearchParameter-searchparameter-endpoint-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/Endpoint?identifier-assigner=[id]`

      *Support:* MAY support search by the [`endpoint-identifier-assigner`](SearchParameter-searchparameter-endpoint-identifier-assigner.html) parameter 
   - with a target type:  `Organization` 
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `identifier`, `name` 
<hr />
1. `GET [base]/Endpoint?mime-type=[code]`

      *Support:* MAY support search by the [`endpoint-mime-type`](SearchParameter-searchparameter-endpoint-mime-type.html) parameter     
<hr />
1. `GET [base]/Endpoint?organization=[id]`

      *Support:* SHALL support search by the [`organization`](SearchParameter-searchparameter-endpoint-organization.html) parameter 
   - with a target type:  `Organization` 
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `identifier`, `name`, `address`, `partof`, `type` 
<hr />
1. `GET [base]/Endpoint?payload-type=[code]`

      *Support:* SHOULD support search by the [`payload-type`](SearchParameter-searchparameter-endpoint-payload-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Endpoint?status=[code]`

      *Support:* SHALL support search by the `status` parameter: `http://hl7.org/fhir/SearchParameter/Endpoint-status`
<hr />
1. `GET [base]/Endpoint?usecase-standard=[uri]`

      *Support:* SHOULD support search by the [`endpoint-usecase-standard`](SearchParameter-searchparameter-endpoint-usecase-standard.html) parameter  
   - including the modifiers:  `below`   
<hr />
1. `GET [base]/Endpoint?usecase-type=[code]`

      *Support:* SHOULD support search by the [`endpoint-usecase-type`](SearchParameter-searchparameter-endpoint-usecase-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Endpoint?via-intermediary=[id]`

      *Support:* MAY support search by the [`endpoint-via-intermediary`](SearchParameter-searchparameter-endpoint-via-intermediary.html) parameter 
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />