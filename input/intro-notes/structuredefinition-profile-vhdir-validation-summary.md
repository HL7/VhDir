#### Complete Summary of the Mandatory Requirements

1.  At least one target in `verificationResult.target`
1.  A coded representation of how often the target is validated in `verificationResult.need`
1.  A coded representation of the target's current validation status in `verificationResult.status`
1.  A date/time when the target's validation status was last updated in `verificationResult.statusDate`
1.  A coded representation of whether the target is validated against a primary source(s) in `verificationResult.validationType`
1.  At least one coded/text representation of the process by which the target was validated in `verificationResult.validationProcess`
1.  A coded representation of what happens if validation of the target fails in `verificationResult.failureAction`
1.  For each primary source described:
    1.  At least one coded/text representation of the type of primary source in `verificationResult.primarySource.type`
1.  Information about the source of the attested information in `VerificationResult.attestation`, including a reference to a Practitioner or Organization resource representing the source of the information in `VerificationResult.attestation.source`
1.  For each validator described:
    1.  One reference to the Organization resource for the validator in `verificationResult.validator.organization`
