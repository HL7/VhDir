#### Supported Searches

1. `GET [base]/CareTeam?category=[code]`

      *Support:* MAY support search by the [`category`](SearchParameter-careteam-category.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/CareTeam?endpoint=[id]`

      *Support:* SHOULD support search by the [`endpoint`](SearchParameter-careteam-endpoint.html) parameter
   - with a target type:  `Endpoint`   
   - including these search paramaters which may be chained:  `endpoint.identifier`, `endpoint.connection-type`, `endpoint.organization`
<hr />
1. `GET [base]/CareTeam?identifier=[code]`

      *Support:* SHALL support search by the [`identifier`](SearchParameter-careteam-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/CareTeam?identifier-assigner=[id]`

      *Support:* MAY support search by the [`identifier-assigner`](SearchParameter-careteam-identifier-assigner.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `identifier-assigner.identifier`, `identifier-assigner.name`
<hr />
1. `GET [base]/CareTeam?location=[id]`

      *Support:* SHALL support search by the [`location`](SearchParameter-careteam-location.html) parameter
   - with a target type:  `Location`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `location.identifier`, `location.type`, `location.address`, `location.organization`
<hr />
1. `GET [base]/CareTeam?participant=[id]`

      *Support:* SHALL support search by the [`participant`](SearchParameter-careteam-participant.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `CareTeam`
   - including the modifier:  `type`  
   - including these search paramaters which may be chained:  `participant.identifier`, `participant.location`, `participant.practitioner`, `participant.organization`, `participant.role`, `participant.address`, `participant.name`, `participant.partof`
<hr />
1. `GET [base]/CareTeam?name=[string]`

      *Support:* SHOULD support search by the [`name`](SearchParameter-careteam-name.html) parameter  
   - including the modifiers:  `exact`, `contains`   
<hr />
1. `GET [base]/CareTeam?organization=[id]`

      *Support:* SHALL support search by the [`organization`](SearchParameter-careteam-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `organization.identifier`, `organization.name`, `organization.address`, `organization.partof`, `organization.type`
<hr />
1. `GET [base]/CareTeam?service=[id]`

      *Support:* SHOULD support search by the [`service`](SearchParameter-careteam-service.html) parameter
   - with a target type:  `HealthcareService`   
   - including these search paramaters which may be chained:  `service.identifier`, `service.service-category`, `service.organization`, `service.location`
<hr />
1. `GET [base]/CareTeam?status=[code]`

      *Support:* SHALL support search by the [`status`](SearchParameter-careteam-status.html) parameter
<hr />
1. `GET [base]/CareTeam?via-intermediary=[id]`

      *Support:* MAY support search by the [`via-intermediary`](SearchParameter-careteam-via-intermediary.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />
