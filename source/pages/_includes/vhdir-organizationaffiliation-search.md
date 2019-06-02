#### Supported Searches

1. `GET [base]/OrganizationAffiliation?active=[code]`

      *Support:* SHALL support search by the `active` parameter: `http://hl7.org/fhir/SearchParameter/OrganizationAffiliation-active`
<hr />
1. `GET [base]/OrganizationAffiliation?organizationaffiliation-endpoint=[id]`

      *Support:* SHOULD support search by the [`organizationaffiliation-endpoint`](SearchParameter-searchparameter-organizationaffiliation-endpoint.html) parameter
   - with a target type:  `Endpoint`   
   - including these search paramaters which may be chained:  `endpoint-identifier`, `endpoint-connection-type`, `endpoint-organization`
<hr />
1. `GET [base]/OrganizationAffiliation?organizationaffiliation-identifier=[code]`

      *Support:* SHALL support search by the [`organizationaffiliation-identifier`](SearchParameter-searchparameter-organizationaffiliation-identifier.html) parameter
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/Organization?organizationaffiliation-identifier-assigner=[id]`

      *Support:* MAY support search by the [`organizationaffiliation-identifier-assigner`](SearchParameter-searchparameter-organizationaffiliation-identifier-assigner.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`
<hr />
1. `GET [base]/OrganizationAffiliation?organizationaffiliation-location=[id]`

      *Support:* SHALL support search by the [`organizationaffiliation-location`](SearchParameter-searchparameter-organizationaffiliation-location.html) parameter
   - with a target type:  `Location`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `location-identifier`, `location-type`, `location-address`, `location-organization`
<hr />
1. `GET [base]/OrganizationAffiliation?organizationaffiliation-network=[id]`

      *Support:* SHOULD support search by the [`organizationaffiliation-network`](SearchParameter-searchparameter-organizationaffiliation-network.html) parameter
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`, `organization-partof`
<hr />
1. `GET [base]/OrganizationAffiliation?organizationaffiliation-participating-organization=[id]`

      *Support:* SHALL support search by the [`organizationaffiliation-participating-organization`](SearchParameter-organizationaffiliation-participating-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`, `organization-address`, `organization-partof`, `organization-type`
<hr />
1. `GET [base]/OrganizationAffiliation?organizationaffiliation-primary-organization=[id]`

      *Support:* SHALL support search by the [`organizationaffiliation-primary-organization`](SearchParameter-searchparameter-organizationaffiliation-primary-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-type`, `organization-address`, `organization-name`, `organization-partof`
<hr />
1. `GET [base]/OrganizationAffiliation?organizationaffiliation-role=[code]`

      *Support:* SHALL support search by the [`organizationaffiliation-role`](SearchParameter-searchparameter-organizationaffiliation-role.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/OrganizationAffiliation?organizationaffiliation-service=[id]`

      *Support:* SHOULD support search by the [`organizationaffiliation-service`](SearchParameter-searchparameter-organizationaffiliation-service.html) parameter
   - with a target type:  `HealthcareService`   
   - including these search paramaters which may be chained:  `identifier`, `service-category`, `organization`, `location`
<hr />
1. `GET [base]/OrganizationAffiliation?organizationaffiliation-specialty=[code]`

      *Support:* SHOULD support search by the [`organizationaffiliation-specialty`](SearchParameter-searchparameter-organizationaffiliation-specialty.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Organization?organizationaffiliation-via-intermediary=[id]`

      *Support:* MAY support search by the [`organizationaffiliation-via-intermediary`](SearchParameter-searchparameter-organizationaffiliation-via-intermediary.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />
