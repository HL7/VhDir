#### Supported Searches

1. `GET [base]/Endpoint?connection-type=[code]`

      *Support:* SHALL support search by the [`connection-type`](SearchParameter-endpoint-connection-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Endpoint?identifier=[code]`

      *Support:* SHALL support search by the [`identifier`](SearchParameter-endpoint-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/Endpoint?identifier-assigner=[id]`

      *Support:* MAY support search by the [`identifier-assigner`](SearchParameter-endpoint-identifier-assigner.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`
<hr />
1. `GET [base]/Endpoint?mime-type=[code]`

      *Support:* MAY support search by the [`mime-type`](SearchParameter-endpoint-mime-type.html) parameter     
<hr />
1. `GET [base]/Endpoint?organization=[id]`

      *Support:* SHALL support search by the [`organization`](SearchParameter-endpoint-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `organization.identifier`, `organization.name`, `organization.address`, `organization.partof`, `organization-type`
<hr />
1. `GET [base]/Endpoint?payload-type=[code]`

      *Support:* SHOULD support search by the [`payload-type`](SearchParameter-endpoint-payload-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Endpoint?status=[code]`

      *Support:* SHALL support search by the [`status`](SearchParameter-endpoint-status.html) parameter
<hr />
1. `GET [base]/Endpoint?usecase-standard=[uri]`

      *Support:* SHOULD support search by the [`usecase-standard`](SearchParameter-endpoint-usecase-standard.html) parameter  
   - including the modifiers:  `below`   
<hr />
1. `GET [base]/Endpoint?usecase-type=[code]`

      *Support:* SHOULD support search by the [`usecase-type`](SearchParameter-endpoint-usecase-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Endpoint?via-intermediary=[id]`

      *Support:* MAY support search by the [`via-intermediary`](SearchParameter-endpoint-via-intermediary.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />
