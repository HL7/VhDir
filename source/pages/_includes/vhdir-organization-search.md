#### Supported Searches

1. `GET [base]/Organization?active=[code]`

      *Support:* SHALL support search by the `active` parameter: `http://hl7.org/fhir/SearchParameter/Organization-active`
<hr />
1. `GET [base]/Organization?address-use=[code]`

      *Support:* MAY support search by the `use` parameter: `http://hl7.org/fhir/SearchParameter/Organization-use`
<hr />
1. `GET [base]/Organization?coverage-area=[id]`

      *Support:* SHOULD support search by the [`network-coverage-area`](SearchParameter-searchparameter-network-coverage-area.html) parameter 
   - with a target type:  `Location`   
   - including these search paramaters which may be chained:  `identifier`, `region` 
<hr />
1. `GET [base]/Network?via-intermediary=[id]`

      *Support:* MAY support search by the [`network-via-intermediary`](SearchParameter-searchparameter-network-via-intermediary.html) parameter 
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />
1. `GET [base]/Organization?address=[string]`

      *Support:* SHALL support search by the [`address`](SearchParameter-searchparameter-organization-address.html) parameter  
   - including the modifiers:  `contains`, `exact`   
<hr />
1. `GET [base]/Organization?address-city=[string]`

      *Support:* SHOULD support search by the [`address-city`](SearchParameter-searchparameter-organization-address-city.html) parameter  
   - including the modifiers:  `exact`   
<hr />
1. `GET [base]/Organization?address-country=[string]`

      *Support:* SHOULD support search by the [`address-country`](SearchParameter-searchparameter-organization-address-country.html) parameter  
   - including the modifiers:  `exact`   
<hr />
1. `GET [base]/Organization?address-postalcode=[string]`

      *Support:* SHOULD support search by the [`address-postalcode`](SearchParameter-searchparameter-organization-address-postalcode.html) parameter  
   - including the modifiers:  `exact`   
<hr />
1. `GET [base]/Organization?address-state=[string]`

      *Support:* SHOULD support search by the [`address-state`](SearchParameter-searchparameter-organization-address-state.html) parameter  
   - including the modifiers:  `exact`   
<hr />
1. `GET [base]/Organization?endpoint=[id]`

      *Support:* SHALL support search by the [`endpoint`](SearchParameter-searchparameter-organization-endpoint.html) parameter 
   - with a target type:  `Endpoint`   
   - including these search paramaters which may be chained:  `identifier`, `connection-type`, `organization` 
<hr />
1. `GET [base]/Organization?identifier=[code]`

      *Support:* SHALL support search by the [`identifier`](SearchParameter-searchparameter-organization-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`   
<hr />
1. `GET [base]/Organization?identifier-assigner=[id]`

      *Support:* MAY support search by the [`organization-identifier-assigner`](SearchParameter-searchparameter-organization-identifier-assigner.html) parameter 
   - with a target type:  `Organization` 
   - including the modifiers:  ` below`  
   - including these search paramaters which may be chained:  `identifier`, `name` 
<hr />
1. `GET [base]/Organization?name=[string]`

      *Support:* SHALL support search by the [`name`](SearchParameter-searchparameter-organization-name.html) parameter  
   - including the modifiers:  `exact`, `contains`   
<hr />
1. `GET [base]/Organization?partof=[id]`

      *Support:* SHALL support search by the [`partof`](SearchParameter-searchparameter-organization-partof.html) parameter 
   - with a target type:  `Organization` 
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`, `organization-address`, `organization-type` 
<hr />
1. `GET [base]/Organization?qualification-code=[code]`

      *Support:* SHOULD support search by the [`organization-qualification-code`](SearchParameter-searchparameter-organization-qualification-code.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Organization?qualification-issuer=[id]`

      *Support:* MAY support search by the [`organization-qualification-issuer`](SearchParameter-searchparameter-organization-qualification-issuer.html) parameter 
   - with a target type:  `Organization` 
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `identifier`, `name` 
<hr />
1. `GET [base]/Organization?qualification-status=[code]`

      *Support:* SHALL support search by the [`organization-qualification-status`](SearchParameter-searchparameter-organization-qualification-status.html) parameter     
<hr />
1. `GET [base]/Organization?qualification-wherevalid-code=[code]`

      *Support:* SHOULD support search by the [`organization-qualification-wherevalid-code`](SearchParameter-searchparameter-organization-qualification-wherevalid-code.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Organization?qualification-wherevalid-location=[id]`

      *Support:* SHOULD support search by the [`organization-qualification-wherevalid-location`](SearchParameter-searchparameter-organization-qualification-wherevalid-location.html) parameter 
   - with a target type:  `Location` 
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `identifier`, `organization` 
<hr />
1. `GET [base]/Organization?type=[code]`

      *Support:* SHALL support search by the [`type`](SearchParameter-searchparameter-organization-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/Organization?via-intermediary=[id]`

      *Support:* MAY support search by the [`organization-via-intermediary`](SearchParameter-searchparameter-organization-via-intermediary.html) parameter 
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
<hr />