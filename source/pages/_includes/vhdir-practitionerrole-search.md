#### Supported Searches

1. `GET [base]/PractitionerRole?active=[code]`

      *Support:* SHALL support search by the `active` parameter: `http://hl7.org/fhir/SearchParameter/PractitionerRole-active`
<hr />
1. `GET [base]/PractitionerRole?practitionerrole-endpoint=[id]`

      *Support:* SHOULD support search by the [`practitionerrole-endpoint`](SearchParameter-searchparameter-practitionerrole-endpoint.html) parameter
   - with a target type:  `Endpoint`   
   - including these search paramaters which may be chained:  `endpoint-identifier`, `endpoint-connection-type`, `endpoint-organization`
<hr />
1. `GET [base]/PractitionerRole?practitionerrole-identifier=[code]`

      *Support:* SHALL support search by the [`practitionerrole-identifier`](SearchParameter-searchparameter-practitionerrole-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/PractitionerRole?practitionerrole-identifier-assigner=[id]`

      *Support:* MAY support search by the [`practitionerrole-identifier-assigner`](SearchParameter-searchparameter-practitionerrole-identifier-assigner.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`
<hr />
1. `GET [base]/PractitionerRole?practitionerrole-location=[id]`

      *Support:* SHALL support search by the [`practitionerrole-location`](SearchParameter-searchparameter-practitionerrole-location.html) parameter
   - with a target type:  `Location`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `location-identifier`, `location-type`, `location-address`, `location-organization`
<hr />
1. `GET [base]/PractitionerRole?practitionerrole-network=[id]`

      *Support:* SHOULD support search by the [`practitionerrole-network`](SearchParameter-searchparameter-practitionerrole-network.html) parameter
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`, `organization-partof`
<hr />
1. `GET [base]/PractitionerRole?practitionerrole-new-patient=[code]`

      *Support:* SHOULD support search by the [`practitionerrole-new-patient`](SearchParameter-searchparameter-practitionerrole-new-patient.html) parameter     
<hr />
1. `GET [base]/PractitionerRole?practitionerrole-new-patient-network=[id]`

      *Support:* SHOULD support search by the [`practitionerrole-new-patient-network`](SearchParameter-searchparameter-practitionerrole-new-patient-network.html) parameter
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`, `organization-partof`
<hr />
1. `GET [base]/PractitionerRole?practitionerrole-organization=[id]`

      *Support:* SHALL support search by the [`practitionerrole-organization`](SearchParameter-searchparameter-practitionerrole-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`, `organization-address`, `organization-partof`, `organization-type`
<hr />
1. `GET [base]/PractitionerRole?practitionerrole-practitioner=[id]`

      *Support:* SHALL support search by the [`practitionerrole-practitioner`](SearchParameter-searchparameter-practitionerrole-practitioner.html) parameter
   - with a target type:  `Practitioner`   
   - including these search paramaters which may be chained:  `practitioner-identifier`, `practitioner-name`
<hr />
1. `GET [base]/PractitionerRole?practitionerrole-qualification-code=[code]`

      *Support:* SHOULD support search by the [`practitionerrole-qualification-code`](SearchParameter-searchparameter-practitionerrole-qualification-code.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/PractitionerRole?practitionerrole-qualification-issuer=[id]`

      *Support:* MAY support search by the [`practitionerrole-qualification-issuer`](SearchParameter-searchparameter-practitionerrole-qualification-issuer.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`
<hr />
1. `GET [base]/PractitionerRole?practitionerrole-qualification-status=[code]`

      *Support:* SHOULD support search by the [`practitionerrole-qualification-status`](SearchParameter-searchparameter-practitionerrole-qualification-status.html) parameter     
<hr />
1. `GET [base]/PractitionerRole?practitionerrole-qualification-wherevalid-code=[code]`

      *Support:* SHOULD support search by the [`practitionerrole-qualification-wherevalid-code`](SearchParameter-searchparameter-practitionerrole-qualification-wherevalid-code.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/PractitionerRole?practitionerrole-qualification-wherevalid=[id]`

      *Support:* SHOULD support search by the [`practitionerrole-qualification-wherevalid`](SearchParameter-searchparameter-practitionerrole-qualification-wherevalid.html) parameter
   - with a target type:  `Location`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `location-identifier`, `location-address`, `location-organization`
<hr />
1. `GET [base]/PractitionerRole?practitionerrole-role=[code]`

      *Support:* SHALL support search by the [`practitionerrole-role`](SearchParameter-searchparameter-practitionerrole-role.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/PractitionerRole?practitionerrole-service=[id]`

      *Support:* SHOULD support search by the [`practitionerrole-service`](SearchParameter-searchparameter-practitionerrole-service.html) parameter
   - with a target type:  `HealthcareService`   
   - including these search paramaters which may be chained:  `healthcareservice-identifier`, `healthcareservice-category`, `healthcareservice-organization`, `healthcareservice-location`
<hr />
1. `GET [base]/PractitionerRole?practitionerrole-specialty=[code]`

      *Support:* SHOULD support search by the [`practitionerrole-specialty`](SearchParameter-searchparameter-practitionerrole-specialty.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/PractitionerRole?practitionerrole-via-intermediary=[id]`

      *Support:* MAY support search by the [`practitionerrole-via-intermediary`](SearchParameter-searchparameter-practitionerrole-via-intermediary.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />
