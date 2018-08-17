#### Supported Searches

1. `GET [base]/VerificationResult?target=[id]`

      *Support:* SHALL support search by the target parameter: `http://hl7.org/fhir/SearchParameter/VerificationResult-target`
   - with a target type:  `Any`
<hr />
1. `GET [base]/Vergit puificationResult?attestation-source=[id]`

      *Support:* SHALL support search by the [`verificationresult-attestation-attester`](SearchParameter-searchparameter-verificationresult-attestation-attester.html) parameter
   - with a target type:  `Practitioner`, `Organization`
   - including the modifiers:  `type`  
   - including these search paramaters which may be chained:  `identifier`, `address`, `name`, `partof`, `practitioner-identifier`, `practitioner-name`
<hr />
1. `GET [base]/VerificationResult?attestation-method=[code]`

      *Support:* SHOULD support search by the [`verificationresult-attestation-method`](SearchParameter-searchparameter-verificationresult-attestation-method.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/VerificationResult?attestation-organization=[id]`

      *Support:* SHALL support search by the [`verificationresult-attestation-proxy`](SearchParameter-searchparameter-verificationresult-attestation-proxy.html) parameter
   - with a target type:  `Practitioner`   
   - including these search paramaters which may be chained:  `practitioner-identifier`, `practitioner-name`
<hr />
1. `GET [base]/VerificationResult?primarysource-date=[dateTime]`

      *Support:* SHOULD support search by the [`organization-qualification-issuer`](SearchParameter-searchparameter-organization-qualification-issuer.html) parameter   
   - including the comparators:  `eq`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`  
<hr />
1. `GET [base]/VerificationResult?primarysource-organization=[id]`

      *Support:* SHALL support search by the [`verificationresult-primarysource-organization`](SearchParameter-searchparameter-verificationresult-primarysource-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `identifier`, `name`
<hr />
1. `GET [base]/VerificationResult?primarysource-type=[code]`

      *Support:* SHOULD support search by the [`verificationresult-primarysource-type`](SearchParameter-searchparameter-verificationresult-primarysource-type.html) parameter  
   - including the modifiers:  `text`   
<hr />
1. `GET [base]/VerificationResult?status-date=[dateTime]`

      *Support:* SHOULD support search by the [`verificationresult-status-date`](SearchParameter-searchparameter-verificationresult-status-date.html) parameter   
   - including the comparators:  `eq`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`  
<hr />
1. `GET [base]/VerificationResult?target-location=[string]`

      *Support:* SHALL support search by the [`verificationresult-target-location`](SearchParameter-searchparameter-verificationresult-target-location.html) parameter  
   - including the modifiers:  `exact`, `contains`   
<hr />
1. `GET [base]/VerificationResult?status=[code]`

      *Support:* SHALL support search by the [`verificationresult-validation-status`](SearchParameter-searchparameter-verificationresult-validation-status.html) parameter     
<hr />
1. `GET [base]/VerificationResult?validator-organization=[id]`

      *Support:* SHALL support search by the [`verificationresult-validator-organization`](SearchParameter-searchparameter-verificationresult-validator-organization.html) parameter
   - with a target type:  `Organization`
   - including the modifiers:  `above`, `below`  
   - including these search paramaters which may be chained:  `identifier`, `name`
<hr />
