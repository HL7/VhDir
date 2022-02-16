#### Supported Searches

1. `GET [base]/PractitionerRole?active=[code]`

      *Support:* SHALL support search by the `active` parameter: `http://hl7.org/fhir/SearchParameter/PractitionerRole-active`
<hr />
1. `GET [base]/PractitionerRole?endpoint=[id]`

      *Support:* SHOULD support search by the [`endpoint`](SearchParameter-practitionerrole-endpoint.html) parameter
   - with a target type:  `Endpoint`   
   - including these search paramaters which may be chained:  `endpoint.identifier`, `endpoint.connection-type`, `endpoint.organization`
<hr />
1. `GET [base]/PractitionerRole?identifier=[code]`

      *Support:* SHALL support search by the [`identifier`](SearchParameter-practitionerrole-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/PractitionerRole?identifier-assigner=[id]`

      *Support:* MAY support search by the [`identifier-assigner`](SearchParameter-practitionerrole-identifier-assigner.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `identifier-assigner.identifier`, `identifier-assigner.name`
<hr />
1. `GET [base]/PractitionerRole?location=[id]`

      *Support:* SHALL support search by the [`location`](SearchParameter-practitionerrole-location.html) parameter
   - with a target type:  `Location`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `location.identifier`, `location.type`, `location.address`, `location.organization`
<hr />
1. `GET [base]/PractitionerRole?network=[id]`

      *Support:* SHOULD support search by the [`network`](SearchParameter-practitionerrole-network.html) parameter
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `network.identifier`, `network.name`, `network.partof`
<hr />
1. `GET [base]/PractitionerRole?new-patient=[code]`

      *Support:* SHOULD support search by the [`new-patient`](SearchParameter-practitionerrole-new-patient.html) parameter     
<hr />
1. `GET [base]/PractitionerRole?new-patient-network=[id]`

      *Support:* SHOULD support search by the [`new-patient-network`](SearchParameter-practitionerrole-new-patient-network.html) parameter
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `new-patient-network.identifier`, `new-patient-network.name`, `new-patient-network.partof`
<hr />
1. `GET [base]/PractitionerRole?organization=[id]`

      *Support:* SHALL support search by the [`organization`](SearchParameter-practitionerrole-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `organization.identifier`, `organization.name`, `organization.address`, `organization.partof`, `organization-type`
<hr />
1. `GET [base]/PractitionerRole?practitioner=[id]`

      *Support:* SHALL support search by the [`practitioner`](SearchParameter-practitionerrole-practitioner.html) parameter
   - with a target type:  `Practitioner`   
   - including these search paramaters which may be chained:  `practitioner.identifier`, `practitioner.name`
<hr />
1. `GET [base]/PractitionerRole?qualification-code=[code]`

      *Support:* SHOULD support search by the [`qualification-code`](SearchParameter-practitionerrole-qualification-code.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/PractitionerRole?qualification-issuer=[id]`

      *Support:* MAY support search by the [`qualification-issuer`](SearchParameter-practitionerrole-qualification-issuer.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `qualification-issuer.identifier`, `qualification-issuer.name`
<hr />
1. `GET [base]/PractitionerRole?qualification-status=[code]`

      *Support:* SHOULD support search by the [`qualification-status`](SearchParameter-practitionerrole-qualification-status.html) parameter     
<hr />
1. `GET [base]/PractitionerRole?qualification-wherevalid-code=[code]`

      *Support:* SHOULD support search by the [`qualification-wherevalid-code`](SearchParameter-practitionerrole-qualification-wherevalid-code.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/PractitionerRole?qualification-wherevalid-location=[id]`

      *Support:* SHOULD support search by the [`qualification-wherevalid-location`](SearchParameter-practitionerrole-qualification-wherevalid-location.html) parameter
   - with a target type:  `Location`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `qualification-wherevalid-location.identifier`, `qualification-wherevalid-location.address`, `qualification-wherevalid-location.organization`
<hr />
1. `GET [base]/PractitionerRole?role=[code]`

      *Support:* SHALL support search by the [`role`](SearchParameter-practitionerrole-role.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/PractitionerRole?service=[id]`

      *Support:* SHOULD support search by the [`service`](SearchParameter-practitionerrole-service.html) parameter
   - with a target type:  `HealthcareService`   
   - including these search paramaters which may be chained:  `service.identifier`, `service.service-category`, `service.organization`, `service.location`
<hr />
1. `GET [base]/PractitionerRole?specialty=[code]`

      *Support:* SHOULD support search by the [`specialty`](SearchParameter-practitionerrole-specialty.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/PractitionerRole?via-intermediary=[id]`

      *Support:* MAY support search by the [`via-intermediary`](SearchParameter-practitionerrole-via-intermediary.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />
