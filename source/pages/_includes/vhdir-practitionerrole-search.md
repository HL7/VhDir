#### Supported Searches

1. `GET [base]/PractitionerRole?active=[code]`

      *Support:* SHALL support search by the `active` parameter: `http://hl7.org/fhir/SearchParameter/PractitionerRole-active`
<hr />
1. `GET [base]/PractitionerRole?endpoint=[id]`

      *Support:* SHOULD support search by the [`endpoint`](SearchParameter-searchparameter-practitionerrole-endpoint.html) parameter
   - with a target type:  `Endpoint`   
   - including these search paramaters which may be chained:  `identifier`, `connection-type`, `organization`
<hr />
1. `GET [base]/PractitionerRole?identifier=[code]`

      *Support:* SHALL support search by the [`identifier`](SearchParameter-searchparameter-practitionerrole-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/PractitionerRole?identifier-assigner=[id]`

      *Support:* MAY support search by the [`practitionerrole-identifier-assigner`](SearchParameter-searchparameter-practitionerrole-identifier-assigner.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `identifier`, `name`
<hr />
1. `GET [base]/PractitionerRole?location=[id]`

      *Support:* SHALL support search by the [`location`](SearchParameter-searchparameter-practitionerrole-location.html) parameter
   - with a target type:  `Location`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `identifier`, `type`, `address`, `organization`
<hr />
1. `GET [base]/PractitionerRole?network=[id]`

      *Support:* SHOULD support search by the [`practitionerrole-network`](SearchParameter-searchparameter-practitionerrole-network.html) parameter
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `identifier`, `name`, `partof`
<hr />
1. `GET [base]/PractitionerRole?new-patient=[code]`

      *Support:* SHOULD support search by the [`practitionerrole-new-patient`](SearchParameter-searchparameter-practitionerrole-new-patient.html) parameter     
<hr />
1. `GET [base]/PractitionerRole?new-patient-network=[id]`

      *Support:* SHOULD support search by the [`practitionerrole-new-patient-network`](SearchParameter-searchparameter-practitionerrole-new-patient-network.html) parameter
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `identifier`, `name`, `partof`
<hr />
1. `GET [base]/PractitionerRole?organization=[id]`

      *Support:* SHALL support search by the [`organization`](SearchParameter-searchparameter-practitionerrole-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `identifier`, `name`, `address`, `partof`, `type`
<hr />
1. `GET [base]/PractitionerRole?practitioner=[id]`

      *Support:* SHALL support search by the [`practitioner`](SearchParameter-searchparameter-practitionerrole-practitioner.html) parameter
   - with a target type:  `Practitioner`   
   - including these search paramaters which may be chained:  `identifier`, `name`
<hr />
1. `GET [base]/PractitionerRole?qualification-code=[code]`

      *Support:* SHOULD support search by the [`practitionerrole-qualification-code`](SearchParameter-searchparameter-practitionerrole-qualification-code.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/PractitionerRole?qualification-issuer=[id]`

      *Support:* MAY support search by the [`practitionerrole-qualification-issuer`](SearchParameter-searchparameter-practitionerrole-qualification-issuer.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `identifier`, `name`
<hr />
1. `GET [base]/PractitionerRole?qualification-status=[code]`

      *Support:* SHALL support search by the [`practitionerrole-qualification-status`](SearchParameter-searchparameter-practitionerrole-qualification-status.html) parameter     
<hr />
1. `GET [base]/PractitionerRole?qualification-wherevalid-code=[code]`

      *Support:* SHOULD support search by the [`practitionerrole-qualification-wherevalid-code`](SearchParameter-searchparameter-practitionerrole-qualification-wherevalid-code.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/PractitionerRole?qualification-wherevalid-location=[id]`

      *Support:* SHOULD support search by the [`practitionerrole-qualification-wherevalid`](SearchParameter-searchparameter-practitionerrole-qualification-wherevalid.html) parameter
   - with a target type:  `Location`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `identifier`, `address`, `organization`
<hr />
1. `GET [base]/PractitionerRole?role=[code]`

      *Support:* SHALL support search by the [`role`](SearchParameter-searchparameter-practitionerrole-role.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/PractitionerRole?service=[id]`

      *Support:* SHOULD support search by the [`service`](SearchParameter-searchparameter-practitionerrole-service.html) parameter
   - with a target type:  `HealthcareService`   
   - including these search paramaters which may be chained:  `identifier`, `category`, `organization`, `location`
<hr />
1. `GET [base]/PractitionerRole?specialty=[code]`

      *Support:* SHOULD support search by the [`specialty`](SearchParameter-searchparameter-practitionerrole-specialty.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/PractitionerRole?via-intermediary=[id]`

      *Support:* MAY support search by the [`practitionerrole-via-intermediary`](SearchParameter-searchparameter-practitionerrole-via-intermediary.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />
