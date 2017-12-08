#### Complete Summary of the Mandatory Requirements

1.  At least one target in `validation.target`
1.  One indication of what happens if validation of the target fails in `validation.failureAction`
1.  For each primary source described:
    1.  At least one type of primary source in `validation.primarySource.sourceType`
    1.  At least one indication of the primary source validation process in `validation.primarySource.sourceValidationProcess`
    1.  One indication of whether the primary source can push updates/alerts in `validation.primarySource.sourcePush`
1.  For each attestation source described:
    1.  One individual that attested to the target information in `validation.attestation.attestationSource`
1.  For each validator described:
    1.  One reference to the organization resource for the validator in `validation.validator.validatorOrg`