#### Supported Searches

1. `GET [base]/Practitioner?active=[code]`

      *Support:* SHALL support search by the `active` parameter: `http://hl7.org/fhir/SearchParameter/Practitioner-active`
<hr />
1. `GET [base]/Practitioner?endpoint=[id]`

      *Support:* MAY support search by the [`endpoint`](SearchParameter-practitioner-endpoint.html) parameter
   - with a target type:  `Endpoint`
   - including these search paramaters which may be chained:  `endpoint.identifier`
<hr />
1. `GET [Base]/Practitioner?family=[string]`

      *Support:* SHOULD support search by the [`family`](SearchParameter-practitioner-family-name.html) parameter  
   - including the modifiers:  `exact`
<hr />
1. `GET [Base]/Practitioner?given=[string]`

      *Support:* SHOULD support search by the [`given`](SearchParameter-practitioner-given-name.html) parameter  
   - including the modifiers:  `exact`
<hr />
1. `GET [base]/Practitioner?identifier=[code]`

      *Support:* SHALL support search by the [`identifier`](SearchParameter-practitioner-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`
<hr />
1. `GET [base]/Practitioner?identifier-assigner=[id]`

      *Support:* MAY support search by the [`identifier-assigner`](SearchParameter-practitioner-identifier-assigner.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `identifier-assigner.identifier`, `identifier-assigner.name`
<hr />
1. `GET [base]/Practitioner?name=[string]`

      *Support:* SHALL support search by the [`name`](SearchParameter-practitioner-name.html) parameter  
   - including the modifiers:  `contains`, `exact`   
<hr />
1. `GET [base]/Practitioner?phonetic=[string]`

      *Support:* MAY support search by the [`phonetic`](SearchParameter-practitioner-phonetic.html) parameter
<hr />
1. `GET [base]/Practitioner?qualification-code=[code]`

      *Support:* SHOULD support search by the [`qualification-code`](SearchParameter-practitioner-qualification-code.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Practitioner?qualification-issuer=[id]`

      *Support:* MAY support search by the [`qualification-issuer`](SearchParameter-practitioner-qualification-issuer.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `qualification-issuer.identifier`, `qualification-issuer.name`
<hr />
1. `GET [base]/Practitioner?qualification-status=[code]`

      *Support:* SHOULD support search by the [`qualification-status`](SearchParameter-practitioner-qualification-status.html) parameter     
<hr />
1. `GET [base]/Practitioner?qualification-wherevalid-code=[code]`

      *Support:* SHOULD support search by the [`qualification-wherevalid-code`](SearchParameter-practitioner-qualification-wherevalid-code.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Practitioner?qualification-wherevalid-location=[id]`

      *Support:* SHOULD support search by the [`qualification-wherevalid-location`](SearchParameter-practitioner-qualification-wherevalid-location.html) parameter
   - with a target type:  `Location`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `qualification-wherevalid-location.identifier`, `qualification-wherevalid-location.address`, `qualification-wherevalid-location.organization`
<hr />
1. `GET [base]/Practitioner?via-intermediary=[id]`

      *Support:* MAY support search by the [`via-intermediary`](SearchParameter-practitioner-via-intermediary.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />
1. `GET [base]/Practitioner?qualification-period=[string]`

      *Support:* SHALL support search by the [`qualification-period`](SearchParameter-practitioner-qualification-period.html) parameter  
   - including the modifiers:  `exact`, `contains`   
<hr />
