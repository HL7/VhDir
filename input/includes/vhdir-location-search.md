#### Supported Searches

`GET [base]/Location?accessibility=[code]`

*Support:* MAY support search by the [`accessibility`](SearchParameter-location-accessibility.html) parameter
   - including the modifiers:  `text`
<hr />
`GET [base]/Location?address=[string]`

*Support:* SHALL support search by the [`address`](SearchParameter-location-address.html) parameter  
   - including the modifiers:  `contains`, `exact`
<hr />
`GET [base]/Location?endpoint=[id]`

*Support:* SHOULD support search by the [`endpoint`](SearchParameter-location-endpoint.html) parameter
   - with a target type:  `Endpoint`
   - including these search paramaters which may be chained:  `endpoint.identifier`, `endpoint.connection-type`, `endpoint.organization`
<hr />
`GET [base]/Location?identifier=[code]`

*Support:* SHALL support search by the [`identifier`](SearchParameter-location-identifier.html) parameter  
   - including the modifiers:  `text`, `ofType`
<hr />
`GET [base]/Location?identifier-assigner=[id]`

*Support:* MAY support search by the [`identifier-assigner`](SearchParameter-location-identifier-assigner.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `below`  
   - including these search paramaters which may be chained:  `identifier-assigner.identifier`, `identifier-assigner.name`
<hr />
`GET [base]/Location?new-patient=[code]`

*Support:* SHOULD support search by the [`new-patient`](SearchParameter-location-new-patient.html) parameter     
<hr />
`GET [base]/Location?new-patient-network=[id]`

*Support:* SHOULD support search by the [`new-patient-network`](SearchParameter-location-new-patient-network.html) parameter
   - with a target type:  `Organization`   
   - including these search paramaters which may be chained:  `new-patient-network.identifier`, `new-patient-network.name`, `new-patient-network.partof`
<hr />
`GET [base]/Location?organization=[id]`

*Support:* SHALL support search by the [`organization`](SearchParameter-location-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `organization.identifier`, `organization.name`, `organization.address`, `organization.partof`, `organization-type`
<hr />
`GET [base]/Location?partof=[id]`

*Support:* SHOULD support search by the [`partof`](SearchParameter-location-partof.html) parameter
   - with a target type:  `Location`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `identifier`, `type`, `address`, `organization`
<hr />
`GET [base]/Location?contains=-83.694810|42.256500`

*Support:* MAY support search by the [`contains`](SearchParameter-location-contains.html) parameter   

This is a special search parameter which might leverage a systems geo-spatial
features to test that the geocoded point provided 
(expressed as [latitude]|[longitude] using the WGS84 datum)
is contained by the boundary stored in the standard extension `boundary-geojson`

Support for multiple points can also be provided using the `,` syntax which
is interpretted as the location returned in the search contains at least 1 of the
provided co-ordinates.

<hr />
`GET [base]/Location?status=[code]`

*Support:* SHALL support search by the [`status`](SearchParameter-location-status.html) parameter
<hr />
`GET [base]/Location?type=[code]`

*Support:* SHALL support search by the [`type`](SearchParameter-location-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
`GET [base]/Location?via-intermediary=[id]`

*Support:* MAY support search by the [`via-intermediary`](SearchParameter-location-via-intermediary.html) parameter
   - with a target type:  `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`    

<hr />
`GET [base]/Location?near=-83.694810|42.256500|11.20|km`

*Support:* MAY support search by the [`near`](http://hl7.org/fhir/location.html#positional) parameter
