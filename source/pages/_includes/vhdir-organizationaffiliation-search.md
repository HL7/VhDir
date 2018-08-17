#### Supported Searches

1. `GET [base]/OrganizationAffiliation?active=[code]`

      *Support:* SHALL support search by the `active` parameter: `http://hl7.org/fhir/SearchParameter/OrganizationAffiliation-active`
<hr />
1. `GET [base]/OrganizationAffiliation?endpoint=[id]`

      *Support:* SHOULD support search by the [`endpoint`](SearchParameter-searchparameter-organizationaffiliation-endpoint.html) parameter
   - with a target type:  `Endpoint`   
   - including these search paramaters which may be chained:  `identifier`, `connection-type`, `organization`
<hr />
1. `GET [base]/OrganizationAffiliation?identifier=[code]`

      *Support:* SHALL support search by the [`identifier`](SearchParameter-searchparameter-organizationaffiliation-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/Organization?identifier-assigner=[id]`

      *Support:* MAY support search by the [`organizationaffiliation-identifier-assigner`](SearchParameter-searchparameter-organizationaffiliation-identifier-assigner.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `identifier`, `name`
<hr />
1. `GET [base]/OrganizationAffiliation?location=[id]`

      *Support:* SHALL support search by the [`location`](SearchParameter-searchparameter-organizationaffiliation-location.html) parameter
   - with a target type:  `Location`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `identifier`, `type`, `address`, `organization`
<hr />
1. `GET [base]/OrganizationAffiliation?network=[id]`

      *Support:* SHOULD support search by the [`network`](SearchParameter-searchparameter-organizationaffiliation-network.html) parameter
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `identifier`, `name`, `partof`
<hr />
1. `GET [base]/OrganizationAffiliation?participating-organization=[id]`

      *Support:* SHALL support search by the [`participating-organization`](SearchParameter-searchparam-organizationaffiliation-participating-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `identifier`, `name`, `address`, `partof`, `type`
<hr />
1. `GET [base]/OrganizationAffiliation?primary-organization=[id]`

      *Support:* SHALL support search by the [`primary-organization`](SearchParameter-searchparameter-organizationaffiliation-primary-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `identifier`, `type`, `address`, `name`, `partof`
<hr />
1. `GET [base]/OrganizationAffiliation?role=[code]`

      *Support:* SHALL support search by the [`role`](SearchParameter-searchparameter-organizationaffiliation-role.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/OrganizationAffiliation?service=[id]`

      *Support:* SHOULD support search by the [`service`](SearchParameter-searchparameter-organizationaffiliation-service.html) parameter
   - with a target type:  `HealthcareService`   
   - including these search paramaters which may be chained:  `identifier`, `category`, `organization`, `location`
<hr />
1. `GET [base]/OrganizationAffiliation?specialty=[code]`

      *Support:* SHOULD support search by the [`specialty`](SearchParameter-searchparameter-organizationaffiliation-specialty.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Organization?via-intermediary=[id]`

      *Support:* MAY support search by the [`organizationaffiliation-via-intermediary`](SearchParameter-searchparameter-organizationaffiliation-via-intermediary.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />
