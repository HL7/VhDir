#### Supported Searches

1. `GET [base]/CareTeam?endpoint=[id]`

      *Support:* SHOULD support search by the [`careteam-endpoint`](SearchParameter-searchparameter-careteam-endpoint.html) parameter 
   - with a target type:  `Endpoint`   
   - including these search paramaters which may be chained:  `identifier`, `connection-type`, `organization` 
<hr />
1. `GET [base]/CareTeam?identifier=[code]`

      *Support:* SHALL support search by the [`identifier`](SearchParameter-searchparameter-careteam-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/CareTeam?identifier-assigner=[id]`

      *Support:* MAY support search by the [`careteam-identifier-assigner`](SearchParameter-searchparameter-careteam-identifier-assigner.html) parameter 
   - with a target type:  `Organization` 
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `identifier`, `name` 
<hr />
1. `GET [base]/CareTeam?location=[id]`

      *Support:* SHALL support search by the [`careteam-location`](SearchParameter-searchparameter-careteam-location.html) parameter 
   - with a target type:  `Location` 
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `identifier`, `type`, `address`, `organization` 
<hr />
1. `GET [base]/CareTeam?name=[string]`

      *Support:* SHOULD support search by the [`careteam-name`](SearchParameter-searchparameter-careteam-name.html) parameter  
   - including the modifiers:  `exact`, `contains`   
<hr />
1. `GET [base]/CareTeam?organization=[id]`

      *Support:* SHALL support search by the [`careteam-organization`](SearchParameter-searchparameter-careteam-organization.html) parameter 
   - with a target type:  `Organization` 
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `identifier`, `name`, `address`, `partof`, `type` 
<hr />
1. `GET [base]/CareTeam?service=[id]`

      *Support:* SHOULD support search by the [`careteam-service`](SearchParameter-searchparameter-careteam-service.html) parameter 
   - with a target type:  `HealthcareService`   
   - including these search paramaters which may be chained:  `identifier`, `category`, `organization`, `location` 
<hr />
1. `GET [base]/CareTeam?status=[code]`

      *Support:* SHALL support search by the `status` parameter: `http://hl7.org/fhir/SearchParameter/CareTeam-status`
<hr />
1. `GET [base]/CareTeam?via-intermediary=[id]`

      *Support:* MAY support search by the [`careteam-via-intermediary`](SearchParameter-searchparameter-careteam-via-intermediary.html) parameter 
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />
1. `GET [base]/CareTeam?category=[code]`

      *Support:* MAY support search by the [`category`](SearchParameter-searchparameter-careteam-category.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/CareTeam?member=[id]`

      *Support:* SHALL support search by the [`careteam-member`](SearchParameter-searchparameter-careteam-member.html) parameter 
   - with a target type:  `PractitionerRole, Organization, CareTeam`    
<hr />