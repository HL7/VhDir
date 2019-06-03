#### Supported Searches

1. `GET [base]/Organization?active=[code]`

      *Support:* SHALL support search by the `active` parameter: `http://hl7.org/fhir/SearchParameter/Organization-active`
<hr />
1. `GET [base]/Organization?address-use=[code]`

      *Support:* MAY support search by the `address-use` parameter: `http://hl7.org/fhir/SearchParameter/Organization-address-use`
<hr />
1. `GET [base]/Organization?address=[string]`

      *Support:* SHALL support search by the [`address`](SearchParameter-organization-address.html) parameter  
   - including the modifiers:  `contains`, `exact`   
<hr />
1. `GET [base]/Organization?organiztion-address-city=[string]`

      *Support:* SHOULD support search by the [`address-city`](SearchParameter-organization-address-city.html) parameter  
   - including the modifiers:  `exact`   
<hr />
1. `GET [base]/Organization?address-country=[string]`

      *Support:* SHOULD support search by the [`address-country`](SearchParameter-organization-address-country.html) parameter  
   - including the modifiers:  `exact`   
<hr />
1. `GET [base]/Organization?address-postalcode=[string]`

      *Support:* SHOULD support search by the [`address-postalcode`](SearchParameter-organization-address-postalcode.html) parameter
   - including the modifiers:  `exact`   
<hr />
1. `GET [base]/Organization?address-state=[string]`

      *Support:* SHOULD support search by the [`address-state`](SearchParameter-organization-address-state.html) parameter  
   - including the modifiers:  `exact`   
<hr />
1. `GET [base]/Organization?endpoint=[id]`

      *Support:* SHALL support search by the [`endpoint`](SearchParameter-organization-endpoint.html) parameter 
   - with a target type:  `Endpoint`   
   - including these search paramaters which may be chained:  `endpoint.identifier`, `endpoint.connection-type`, `endpoint.organization` 
<hr />
1. `GET [base]/Organization?identifier=[code]`

      *Support:* SHALL support search by the [`identifier`](SearchParameter-organization-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/Organization?identifier-assigner=[id]`

      *Support:* MAY support search by the [`identifier-assigner`](SearchParameter-organization-identifier-assigner.html) parameter 
   - with a target type:  `Organization` 
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `identifier-assigner.identifier`, `identifier-assigner.name` 
<hr />
1. `GET [base]/Organization?name=[string]`

      *Support:* SHALL support search by the [`name`](SearchParameter-organization-name.html) parameter  
   - including the modifiers:  `exact`, `contains`   
<hr />
1. `GET [base]/Organization?partof=[id]`

      *Support:* SHALL support search by the [`partof`](SearchParameter-organization-partof.html) parameter 
   - with a target type:  `Organization` 
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `partof.identifier`, `partof.name`, `partof.address`, `partof.type` 
<hr />
1. `GET [base]/Organization?qualification-code=[code]`

      *Support:* SHOULD support search by the [`qualification-code`](SearchParameter-organization-qualification-code.html) parameter
   - including the modifiers:  `text`
<hr />
1. `GET [base]/Organization?qualification-issuer=[id]`

      *Support:* MAY support search by the [`qualification-issuer`](SearchParameter-organization-qualification-issuer.html) parameter 
   - with a target type:  `Organization` 
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `qualification-issuer.identifier`, `qualification-issuer.name` 
<hr />
1. `GET [base]/Organization?qualification-status=[code]`

      *Support:* SHOULD support search by the [`qualification-status`](SearchParameter-organization-qualification-status.html) parameter     
<hr />
1. `GET [base]/Organization?qualification-wherevalid-code=[code]`

      *Support:* SHOULD support search by the [`qualification-wherevalid-code`](SearchParameter-organization-qualification-wherevalid-code.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Organization?qualification-wherevalid-location=[id]`

      *Support:* SHOULD support search by the [`qualification-wherevalid-location`](SearchParameter-organization-qualification-wherevalid-location.html) parameter 
   - with a target type:  `Location` 
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `qualification-wherevalid-location.identifier`, `qualification-wherevalid-location.organization` 
<hr />
1. `GET [base]/Organization?type=[code]`

      *Support:* SHALL support search by the [`type`](SearchParameter-organization-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Organization?via-intermediary=[id]`

      *Support:* MAY support search by the [`via-intermediary`](SearchParameter-organization-via-intermediary.html) parameter 
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />