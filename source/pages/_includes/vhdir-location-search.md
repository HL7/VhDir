#### Supported Searches

`GET [base]/Location?accessibility=[code]`

*Support:* MAY support search by the [`location-accessibility`](SearchParameter-searchparameter-location-accessibility.html) parameter
   - including the modifiers:  `text`
<hr />
`GET [base]/Location?address=[string]`

*Support:* SHALL support search by the [`location-address`](SearchParameter-searchparameter-location-address.html) parameter  
   - including the modifiers:  `contains`, `exact`
<hr />
`GET [base]/Location?endpoint=[id]`

*Support:* SHOULD support search by the [`location-endpoint`](SearchParameter-searchparameter-location-endpoint.html) parameter
   - with a target type:  `Endpoint`
   - including these search paramaters which may be chained:  `endpoint-identifier`, `endpoint-connection-type`, `endpoint-organization`
<hr />
`GET [base]/Location?identifier=[code]`

*Support:* SHALL support search by the [`location-identifier`](SearchParameter-searchparameter-location-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`
<hr />
`GET [base]/Location?identifier-assigner=[id]`

*Support:* MAY support search by the [`location-identifier-assigner`](SearchParameter-searchparameter-location-identifier-assigner.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`
<hr />
`GET [base]/Location?new-patient=[code]`

*Support:* SHOULD support search by the [`location-new-patient`](SearchParameter-searchparameter-location-new-patient.html) parameter     
<hr />
`GET [base]/Location?new-patient-network=[id]`

*Support:* SHOULD support search by the [`location-new-patient-network`](SearchParameter-searchparameter-location-new-patient-network.html) parameter
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`, `organization-partof`
<hr />
`GET [base]/Location?organization=[id]`

*Support:* SHALL support search by the [`location-organization`](SearchParameter-searchparameter-location-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`, `organization-address`, `organization-partof`, `organization-type`
<hr />
`GET [base]/Location?partof=[id]`

*Support:* SHOULD support search by the [`location-partof`](SearchParameter-searchparameter-location-partof.html) parameter
   - with a target type:  `Location`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `location-identifier`, `location-type`, `location-address`, `location-organization`
<hr />
`GET [base]/Location?contains=-83.694810|42.256500`

*Support:* MAY support search by the [`location-contains`](SearchParameter-searchparameter-location-contains.html) parameter   

This is a special search parameter which might leverage a systems geo-spatial
features to test that the geocoded point provided 
(expressed as [latitude]|[longitude] using the WGS84 datum)
is contained by the boundary stored in the standard extension `location-boundary-geojson`

Support for multiple points can also be provided using the `,` syntax which
is interpretted as the location returned in the search contains at least 1 of the
provided co-ordinates.

<hr />
`GET [base]/Location?status=[code]`

*Support:* SHALL support search by the [`location-status`](SearchParameter-searchparameter-location-status.html) parameter
<hr />
`GET [base]/Location?type=[code]`

*Support:* SHALL support search by the [`location-type`](SearchParameter-searchparameter-location-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
`GET [base]/Location?via-intermediary=[id]`

*Support:* MAY support search by the [`location-via-intermediary`](SearchParameter-searchparameter-location-via-intermediary.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    
