#### Supported Searches

1. `GET [base]/Endpoint?endpoint-connection-type=[code]`

      *Support:* SHALL support search by the [`endpoint-connection-type`](SearchParameter-endpoint-connection-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Endpoint?endpoint-identifier=[code]`

      *Support:* SHALL support search by the [`endpoint-identifier`](SearchParameter-endpoint-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/Endpoint?endpoint-identifier-assigner=[id]`

      *Support:* MAY support search by the [`endpoint-identifier-assigner`](SearchParameter-endpoint-identifier-assigner.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`
<hr />
1. `GET [base]/Endpoint?endpoint-mime-type=[code]`

      *Support:* MAY support search by the [`endpoint-mime-type`](SearchParameter-endpoint-mime-type.html) parameter     
<hr />
1. `GET [base]/Endpoint?endpoint-organization=[id]`

      *Support:* SHALL support search by the [`endpoint-organization`](SearchParameter-endpoint-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`, `organization-address`, `organization-partof`, `organization-type`
<hr />
1. `GET [base]/Endpoint?endpoint-payload-type=[code]`

      *Support:* SHOULD support search by the [`endpoint-payload-type`](SearchParameter-endpoint-payload-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Endpoint?endpoint-status=[code]`

      *Support:* SHALL support search by the [`endpoint-status`](SearchParameter-endpoint-status.html) parameter
<hr />
1. `GET [base]/Endpoint?endpoint-usecase-standard=[uri]`

      *Support:* SHOULD support search by the [`endpoint-usecase-standard`](SearchParameter-endpoint-usecase-standard.html) parameter  
   - including the modifiers:  `below`   
<hr />
1. `GET [base]/Endpoint?endpoint-usecase-type=[code]`

      *Support:* SHOULD support search by the [`endpoint-usecase-type`](SearchParameter-endpoint-usecase-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Endpoint?endpoint-via-intermediary=[id]`

      *Support:* MAY support search by the [`endpoint-via-intermediary`](SearchParameter-endpoint-via-intermediary.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />
