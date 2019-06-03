#### Supported Searches

1. `GET [base]/VerificationResult?attestation-who=[id]`

      *Support:* SHALL support search by the [`attestation-who`](SearchParameter-verificationresult-attestation-who.html) parameter
   - with a target type:  `Practitioner`, `Organization`, `PractitionerRole`
   - including the modifiers:  `type`
   - including these search paramaters which may be chained:  `attestation-who.identifier`, `attestation-who.address`, `attestation-who.name`, `attestation-who.partof`, `attestation-who.location`, `attestation-who.organization`, `attestation-who.practitioner`
<hr />
1. `GET [base]/VerificationResult?attestation-method=[code]`

      *Support:* SHOULD support search by the [`attestation-method`](SearchParameter-verificationresult-attestation-method.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/VerificationResult?attestation-onbehalfof=[id]`

      *Support:* SHALL support search by the [`attestation-onbehalfof`](SearchParameter-verificationresult-attestation-onbehalfof.html) parameter
   - with a target type:  `Practitioner`, `Organization`, `PractitionerRole`
   - including the modifiers:  `type`
   - including these search paramaters which may be chained:  `attestation-onbehalfof.identifier`, `attestation-onbehalfof.address`, `attestation-onbehalfof.name`, `attestation-onbehalfof.partof`, `attestation-onbehalfof.location`, `attestation-onbehalfof.organization`, `attestation-onbehalfof.practitioner`
<hr />
1. `GET [base]/VerificationResult?primarysource-date=[dateTime]`

      *Support:* SHOULD support search by the [`primarysource-date`](SearchParameter-verificationresult-primarysource-date.html) parameter   
   - including the comparators:  `eq`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`  
<hr />
1. `GET [base]/VerificationResult?primarysource-who=[id]`

      *Support:* SHALL support search by the [`primarysource-who`](SearchParameter-verificationresult-primarysource-who.html) parameter
   - with a target type:  `Practitioner`, `Organization`, `PractitionerRole`
   - including the modifiers:  `type`
   - including these search paramaters which may be chained:  `primarysource-who.identifier`, `primarysource-who.address`, `primarysource-who.name`, `primarysource-who.partof`, `primarysource-who.location`, `primarysource-who.organization`, `primarysource-who.practitioner`
<hr />
1. `GET [base]/VerificationResult?primarysource-type=[code]`

      *Support:* SHOULD support search by the [`primarysource-type`](SearchParameter-verificationresult-primarysource-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/VerificationResult?status-date=[dateTime]`

      *Support:* SHOULD support search by the [`status-date`](SearchParameter-verificationresult-status-date.html) parameter   
   - including the comparators:  `eq`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`  
<hr />
1. `GET [base]/VerificationResult?target=[id]`

      *Support:* SHALL support search by the [`target`](SearchParameter-verificationresult-target.html) parameter
   - with a target type:  `Any`
   - including the modifier: `type`
<hr />
1. `GET [base]/VerificationResult?target-location=[string]`

      *Support:* SHALL support search by the [`target-location`](SearchParameter-verificationresult-target-location.html) parameter  
   - including the modifiers:  `exact`, `contains`   
<hr />
1. `GET [base]/VerificationResult?status=[code]`

      *Support:* SHALL support search by the [`validation-status`](SearchParameter-verificationresult-validation-status.html) parameter     
<hr />
1. `GET [base]/VerificationResult?validator-organization=[id]`

      *Support:* SHALL support search by the [`validator-organization`](SearchParameter-verificationresult-validator-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `validator-organization.identifier`, `validator-organization.name`
<hr />
