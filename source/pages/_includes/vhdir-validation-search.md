#### Supported Searches

1. `GET [base]/VerificationResult?verificationresult-attestation-who=[id]`

      *Support:* SHALL support search by the [`verificationresult-attestation-who`](SearchParameter-verificationresult-attestation-who.html) parameter
   - with a target type:  `Practitioner`, `Organization`, `PractitionerRole`
   - including the modifiers:  `type`
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-address`, `organization-name`, `organization-partof`, `practitioner-identifier`, `practitioner-name`, `practitionerrole-identifier`, `practitionerrole-location`, `practitionerrole-organization`, `practitionerrole-practitioner`
<hr />
1. `GET [base]/VerificationResult?verificationresult-attestation-method=[code]`

      *Support:* SHOULD support search by the [`verificationresult-attestation-method`](SearchParameter-verificationresult-attestation-method.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/VerificationResult?verificationresult-attestation-onbehalfof=[id]`

      *Support:* SHALL support search by the [`verificationresult-attestation-onbehalfof`](SearchParameter-verificationresult-attestation-onbehalfof.html) parameter
   - with a target type:  `Practitioner`, `Organization`, `PractitionerRole`
   - including the modifiers:  `type`
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-address`, `organization-name`, `organization-partof`, `practitioner-identifier`, `practitioner-name`, `practitionerrole-identifier`, `practitionerrole-location`, `practitionerrole-organization`, `practitionerrole-practitioner`
<hr />
1. `GET [base]/VerificationResult?verificationresult-primarysource-date=[dateTime]`

      *Support:* SHOULD support search by the [`verificationresult-primarysource-date`](SearchParameter-verificationresult-primarysource-date.html) parameter   
   - including the comparators:  `eq`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`  
<hr />
1. `GET [base]/VerificationResult?verificationresult-primarysource-who=[id]`

      *Support:* SHALL support search by the [`verificationresult-primarysource-who`](SearchParameter-verificationresult-primarysource-who.html) parameter
   - with a target type:  `Practitioner`, `Organization`, `PractitionerRole`
   - including the modifiers:  `type`
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-address`, `organization-name`, `organization-partof`, `practitioner-identifier`, `practitioner-name`, `practitionerrole-identifier`, `practitionerrole-location`, `practitionerrole-organization`, `practitionerrole-practitioner`
<hr />
1. `GET [base]/VerificationResult?verificationresult-primarysource-type=[code]`

      *Support:* SHOULD support search by the [`verificationresult-primarysource-type`](SearchParameter-verificationresult-primarysource-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/VerificationResult?verificationresult-status-date=[dateTime]`

      *Support:* SHOULD support search by the [`verificationresult-status-date`](SearchParameter-verificationresult-status-date.html) parameter   
   - including the comparators:  `eq`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`  
<hr />
1. `GET [base]/VerificationResult?verificationresult-target=[id]`

      *Support:* SHALL support search by the [`verificationresult-target`](SearchParameter-verificationresult-target.html) parameter
   - with a target type:  `Any`
   - including the modifier: `type`
<hr />
1. `GET [base]/VerificationResult?verificationresult-target-location=[string]`

      *Support:* SHALL support search by the [`verificationresult-target-location`](SearchParameter-verificationresult-target-location.html) parameter  
   - including the modifiers:  `exact`, `contains`   
<hr />
1. `GET [base]/VerificationResult?verificationresult-status=[code]`

      *Support:* SHALL support search by the [`verificationresult-validation-status`](SearchParameter-verificationresult-validation-status.html) parameter     
<hr />
1. `GET [base]/VerificationResult?verificationresult-validator-organization=[id]`

      *Support:* SHALL support search by the [`verificationresult-validator-organization`](SearchParameter-verificationresult-validator-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `organization-identifier`, `organization-name`
<hr />
