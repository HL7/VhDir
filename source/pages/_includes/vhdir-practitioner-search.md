#### Supported Searches

1. `GET [base]/Practitioner?active=[code]`

      *Support:* SHALL support search by the `active` parameter: `http://hl7.org/fhir/SearchParameter/Practitioner-active`
<hr />
1. `GET [base]/Practitioner?practitioner-endpoint=[id]`

      *Support:* MAY support search by the [`practitioner-endpoint`](SearchParameter-searchparameter-practitioner-endpoint.html) parameter
   - with a target type:  `Endpoint`
   - including these search paramaters which may be chained:  `endpoint-identifier`
<hr />
1. `GET [Base]/Practitioner?practitioner-family-name=[string]`

      *Support:* SHOULD support search by the [`practitioner-family-name`](SearchParameter-searchparameter-practitioner-family-name.html) parameter  
   - including the modifiers:  `exact`
<hr />
1. `GET [Base]/Practitioner?practitioner-given-name=[string]`

      *Support:* SHOULD support search by the [`practitioner-given-name`](SearchParameter-searchparameter-practitioner-given-name.html) parameter  
   - including the modifiers:  `exact`
<hr />
1. `GET [base]/Practitioner?practitioner-identifier=[code]`

      *Support:* SHALL support search by the [`practitioner-identifier`](SearchParameter-searchparameter-practitioner-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`
<hr />
1. `GET [base]/Practitioner?identifier-assigner=[id]`

      *Support:* MAY support search by the [`practitioner-identifier-assigner`](SearchParameter-searchparameter-practitioner-identifier-assigner.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`
<hr />
1. `GET [base]/Practitioner?practitioner-name=[string]`

      *Support:* SHALL support search by the [`practitioner-name`](SearchParameter-searchparameter-practitioner-name.html) parameter  
   - including the modifiers:  `contains`, `exact`   
<hr />
1. `GET [base]/Practitioner?practitioner-phonetic=[string]`

      *Support:* MAY support search by the [`practitioner-phonetic`](SearchParameter-searchparameter-practitioner-phonetic.html) parameter
<hr />
1. `GET [base]/Practitioner?practitioner-qualification-code=[code]`

      *Support:* SHOULD support search by the [`practitioner-qualification-code`](SearchParameter-searchparameter-practitioner-qualification-code.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Practitioner?practitioner-qualification-issuer=[id]`

      *Support:* MAY support search by the [`practitioner-qualification-issuer`](SearchParameter-searchparameter-practitioner-qualification-issuer.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`
<hr />
1. `GET [base]/Practitioner?practitioner-qualification-status=[code]`

      *Support:* SHOULD support search by the [`practitioner-qualification-status`](SearchParameter-searchparameter-practitioner-qualification-status.html) parameter     
<hr />
1. `GET [base]/Practitioner?practitioner-qualification-wherevalid-code=[code]`

      *Support:* SHOULD support search by the [`qualification-wherevalid-code`](SearchParameter-practitioner-qualification-wherevalid-code.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Practitioner?practitioner-qualification-wherevalid-location=[id]`

      *Support:* SHOULD support search by the [`practitioner-qualification-wherevalid-location`](SearchParameter-practitioner-qualification-wherevalid-location.html) parameter
   - with a target type:  `Location`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `location-identifier`, `location-address`, `location-organization`
<hr />
1. `GET [base]/Practitioner?practitioner-via-intermediary=[id]`

      *Support:* MAY support search by the [`practitioner-via-intermediary`](SearchParameter-searchparameter-practitioner-via-intermediary.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />
