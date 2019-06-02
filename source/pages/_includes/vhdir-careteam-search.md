#### Supported Searches

1. `GET [base]/CareTeam?careteam-category=[code]`

      *Support:* MAY support search by the [`careteam-category`](SearchParameter-searchparameter-careteam-category.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/CareTeam?careteam-endpoint=[id]`

      *Support:* SHOULD support search by the [`careteam-endpoint`](SearchParameter-searchparameter-careteam-endpoint.html) parameter
   - with a target type:  `Endpoint`   
   - including these search paramaters which may be chained:  `endpoint-identifier`, `endpoint-connection-type`, `endpoint-organization`
<hr />
1. `GET [base]/CareTeam?careteam-identifier=[code]`

      *Support:* SHALL support search by the [`careteam-identifier`](SearchParameter-searchparameter-careteam-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/CareTeam?careteam-identifier-assigner=[id]`

      *Support:* MAY support search by the [`careteam-identifier-assigner`](SearchParameter-searchparameter-careteam-identifier-assigner.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`
<hr />
1. `GET [base]/CareTeam?careteam-location=[id]`

      *Support:* SHALL support search by the [`careteam-location`](SearchParameter-searchparameter-careteam-location.html) parameter
   - with a target type:  `Location`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `location-identifier`, `location-type`, `location-address`, `location-organization`
<hr />
1. `GET [base]/CareTeam?participant=[id]`

      *Support:* SHALL support search by the [`participant`](SearchParameter-careteam-participant.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `CareTeam`
   - including the modifier:  `type`  
   - including these search paramaters which may be chained:  `practitionerrole-identifier`, `practitionerrole-location`, `practitionerrole-practitioner`, `practitionerrole-organization`, `practitionerrole-role`, `organization-address`, `organization-identifier`, `organization-name`, `organization-partof`, `careteam-identifier`, `careteam-location`, `careteam-organization`
<hr />
1. `GET [base]/CareTeam?careteam-name=[string]`

      *Support:* SHOULD support search by the [`careteam-name`](SearchParameter-searchparameter-careteam-name.html) parameter  
   - including the modifiers:  `exact`, `contains`   
<hr />
1. `GET [base]/CareTeam?careteam-organization=[id]`

      *Support:* SHALL support search by the [`careteam-organization`](SearchParameter-searchparameter-careteam-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`, `organization-address`, `organization-partof`, `organization-type`
<hr />
1. `GET [base]/CareTeam?careteam-service=[id]`

      *Support:* SHOULD support search by the [`careteam-service`](SearchParameter-searchparameter-careteam-service.html) parameter
   - with a target type:  `HealthcareService`   
   - including these search paramaters which may be chained:  `identifier`, `service-category`, `organization`, `location`
<hr />
1. `GET [base]/CareTeam?careteam-status=[code]`

      *Support:* SHALL support search by the [`careteam-status`](SearchParameter-searchparameter-careteam-status.html) parameter
<hr />
1. `GET [base]/CareTeam?careteam-via-intermediary=[id]`

      *Support:* MAY support search by the [`careteam-via-intermediary`](SearchParameter-searchparameter-careteam-via-intermediary.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />
