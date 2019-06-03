#### Supported Searches

1. `GET [base]/OrganizationAffiliation?active=[code]`

      *Support:* SHALL support search by the `active` parameter: `http://hl7.org/fhir/SearchParameter/OrganizationAffiliation-active`
<hr />
1. `GET [base]/OrganizationAffiliation?endpoint=[id]`

      *Support:* SHOULD support search by the [`endpoint`](SearchParameter-organizationaffiliation-endpoint.html) parameter
   - with a target type:  `Endpoint`   
   - including these search paramaters which may be chained:  `endpoint.identifier`, `endpoint.connection-type`, `endpoint.organization`
<hr />
1. `GET [base]/OrganizationAffiliation?identifier=[code]`

      *Support:* SHALL support search by the [`identifier`](SearchParameter-organizationaffiliation-identifier.html) parameter
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/Organization?identifier-assigner=[id]`

      *Support:* MAY support search by the [`identifier-assigner`](SearchParameter-organizationaffiliation-identifier-assigner.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `identifier-assigner.identifier`, `identifier-assigner.name`
<hr />
1. `GET [base]/OrganizationAffiliation?location=[id]`

      *Support:* SHALL support search by the [`location`](SearchParameter-organizationaffiliation-location.html) parameter
   - with a target type:  `Location`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `location.identifier`, `location.type`, `location.address`, `location.organization`
<hr />
1. `GET [base]/OrganizationAffiliation?network=[id]`

      *Support:* SHOULD support search by the [`network`](SearchParameter-organizationaffiliation-network.html) parameter
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `network.identifier`, `network.name`, `network.partof`
<hr />
1. `GET [base]/OrganizationAffiliation?participating-organization=[id]`

      *Support:* SHALL support search by the [`participating-organization`](SearchParameter-organizationaffiliation-participating-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `participating-organization.identifier`, `participating-organization.name`, `participating-organization.address`, `participating-organization.partof`, `participating-organization.type`
<hr />
1. `GET [base]/OrganizationAffiliation?primary-organization=[id]`

      *Support:* SHALL support search by the [`primary-organization`](SearchParameter-organizationaffiliation-primary-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `primary-organization.identifier`, `primary-organization.type`, `primary-organization.address`, `primary-organization.name`, `primary-organization.partof`
<hr />
1. `GET [base]/OrganizationAffiliation?role=[code]`

      *Support:* SHALL support search by the [`role`](SearchParameter-organizationaffiliation-role.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/OrganizationAffiliation?service=[id]`

      *Support:* SHOULD support search by the [`service`](SearchParameter-organizationaffiliation-service.html) parameter
   - with a target type:  `HealthcareService`   
   - including these search paramaters which may be chained:  `service.identifier`, `service.service-category`, `service.organization`, `service.location`
<hr />
1. `GET [base]/OrganizationAffiliation?specialty=[code]`

      *Support:* SHOULD support search by the [`specialty`](SearchParameter-organizationaffiliation-specialty.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Organization?via-intermediary=[id]`

      *Support:* MAY support search by the [`via-intermediary`](SearchParameter-organizationaffiliation-via-intermediary.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />
